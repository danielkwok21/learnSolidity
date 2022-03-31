# 1. Import accounts and ConvertEthToUsd from brownie
# accounts is the list of 10 dummy accounts provided by brownie
# ConvertEthToUsd is an array of deployed solidity contract. ConvertEthToUsd[-1] to get latest deployment
from brownie import accounts, ConvertEthToUsd
import time

def main():
    deploy()


def deploy():
    # dev_account1 is a locally imported account.
    # https://eth-brownie.readthedocs.io/en/stable/account-management.html#importing-from-a-private-key
    account = accounts.load("dev_account1")
    print(f"Account selected: {account}")
    
    # 3. Deploy solidity contract
    ConvertEthToUsd_contract = ConvertEthToUsd.deploy({"from": account})

    # 4. Invoke contract function
    price = ConvertEthToUsd_contract.getLatestEthPriceInUsd()

    logger(f"Latest price in usd: {price}")

def logger(message):
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    print(f"[Logger {current_time}] {message}")