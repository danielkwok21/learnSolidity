from scripts.helpful_scripts import get_account
from scripts.get_weth import get_weth
from brownie import network, config, interface
from web3 import Web3
import time


def main():
    account = get_account()
    wei_to_deposit = Web3.toWei(0.001, "ether")
    weth_addr = config["networks"][network.show_active()]["weth_token"]
    dai_addr = config["networks"][network.show_active()]["dai_token"]

    lending_pool = get_lending_pool()

    # 0. Only applicable for mainnet-fork-dev
    #    run get_weth(), because account is newly generated for each run
    #    there is no way to pre-load account with weth by running get_weth() manually beforehand
    if network.show_active() in ["mainnet-fork-dev"]:
        get_weth()

    # 1. Deposit ether into lending_pool
    deposit(wei_to_deposit, lending_pool, weth_addr, account)

    # 2. Figure out how much eth we can borrow
    borrowable_eth = get_borrowable_eth(lending_pool, account)

    # 3. Get conversion rate of dai -> eth. PS no eth -> dai price feed exists
    dai_to_ether_pricefeed_addr = config["networks"][network.show_active(
    )]["dai_to_eth_pricefeed"]
    dai_to_ether_price = get_asset_price_in_eth(dai_to_ether_pricefeed_addr)

    # 4. Calculate amount of dai we can borrow
    #    Set limit to be 95%, so we have a buffer of 5%
    limit = 0.95
    borrowable_dai_in_eth = (borrowable_eth / dai_to_ether_price) * limit
    borrowable_dai_in_wei = Web3.toWei(borrowable_dai_in_eth, "ether")
    logger(f"borrowable_dai_in_wei={borrowable_dai_in_wei}")

    # 5. Borrow dai
    borrow(borrowable_dai_in_wei, lending_pool, dai_addr, account)

    # 6. Review how much we've borrowed, and how much more left we can borrow
    print_account_info(lending_pool, account)


# More info at https://docs.aave.com/developers/v/2.0/the-core-protocol/lendingpool#borrow
def borrow(amount_in_wei, lending_pool, asset_addr, account):
    logger(f"borrow...")
    rate_mode = 1
    referral_code = 0
    tx = lending_pool.borrow(asset_addr, amount_in_wei,
                             rate_mode, referral_code, account.address, {"from": account})
    tx.wait(1)
    logger(f"...borrow")
    return tx


# More info at https://docs.aave.com/developers/v/2.0/the-core-protocol/lendingpool#deposit
def deposit(amount, lending_pool, asset_addr, account):
    logger("deposit...")
    approve_tx(amount, lending_pool.address, asset_addr, account)
    tx = lending_pool.deposit(asset_addr, amount,
                              account.address, 0, {"from": account})
    tx.wait(1)
    logger("...deposit")
    return tx


# Optional
# More info at https://docs.aave.com/developers/v/2.0/the-core-protocol/lendingpool#repay
def repay_borrowed(asset_addr, amount, lending_pool, account):
    logger("repay_borrowed...")
    rate_mode = 1
    approve_tx(amount, lending_pool, asset_addr, account)
    tx = lending_pool.repay(asset_addr, amount, rate_mode,
                            account.address, {"from": account})
    tx.wait(1)
    logger("...repay_borrowed")


# Get conversion rate of any asset, based on pricefeed address provided
def get_asset_price_in_eth(address):
    logger('get_asset_price_in_eth...')
    dai_eth_price_feed = interface.IAggregatorV3(address)
    (
        _, price_in_wei, _, _, _,
    ) = dai_eth_price_feed.latestRoundData()

    price_in_eth = float(Web3.fromWei(price_in_wei, "ether"))

    logger(f'...get_asset_price_in_eth. price_in_eth={price_in_eth}')

    return price_in_eth


# More info at https://docs.aave.com/developers/v/2.0/the-core-protocol/lendingpool#getuseraccountdata
def print_account_info(lending_pool, account):
    logger('print_account_info...')
    (
        total_collateral_wei,
        total_debt_wei,
        borrowable_wei,
        current_liq_threadhold,
        ltv,
        health_factor
    ) = lending_pool.getUserAccountData(account.address, {"from": account})

    logger(f"total_collateral_wei={total_collateral_wei}")
    logger(f"total_debt_wei={total_debt_wei}")
    logger(f"borrowable_wei={borrowable_wei}")
    logger(f"current_liq_threadhold={current_liq_threadhold}")
    logger(f"ltv={ltv}")
    logger(f"health_factor={health_factor}")

    logger(f'...print_account_info.')


# More info at https://docs.aave.com/developers/v/2.0/the-core-protocol/lendingpool#getuseraccountdata
def get_borrowable_eth(lending_pool, account):
    logger('get_borrowable_eth...')
    (
        _,
        _,
        borrowable_wei,
        _,
        _,
        _
    ) = lending_pool.getUserAccountData(account.address, {"from": account})
    borrowable_eth = Web3.fromWei(borrowable_wei, "ether")

    logger(f'...get_borrowable_eth. borrowable_eth = {borrowable_eth}')
    return float(borrowable_eth)


# All transactions to aave lending pool needs to be approved beforehand
# More info at https://medium.com/ethex-market/erc20-approve-allow-explained-88d6de921ce9
def approve_tx(amount, spender, erc20_addr, account):
    logger(f"approve_tx...")
    erc20 = interface.IERC20(erc20_addr)

    tx = erc20.approve(spender, amount, {"from": account})
    tx.wait(1)
    logger(f"...approve_tx")

    return tx


# lending_pool_addr changes over time
# This is why we get it from lending_pool_address_provider
# lending_pool_address_provider_addr -> lending_pool_address_provider -> lending_pool_addr -> lending_pool
# More info at https://docs.aave.com/developers/v/2.0/the-core-protocol/addresses-provider
def get_lending_pool():
    logger('get_lending_pool...')

    lending_pool_address_provider_addr = config["networks"][network.show_active(
    )]["lending_pool_addresses_provider"]
    lending_pool_address_provider = interface.ILendingPoolAddressesProvider(
        lending_pool_address_provider_addr)

    lending_pool_addr = lending_pool_address_provider.getLendingPool()
    lending_pool = interface.ILendingPool(lending_pool_addr)

    logger(f'...get_lending_pool. lending_pool={lending_pool}')
    return lending_pool


def logger(message):
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    print(f"[Logger {current_time}] {message}")
