# 1. Import accounts and MVP from brownie
# accounts is the list of 10 dummy accounts provided by brownie
# MVP is the compiled solidity contract. Can be found in ../contracts/mvp.sol
from brownie import accounts, MVP

def main():
    deploy_local_with_brownie_test_account()


def deploy_local_with_brownie_test_account():
    # 2. Set deploying account to be the first dummy account
    account = accounts[0]
    
    # 3. Deploy solidity contract
    mvp_contract = MVP.deploy({"from": account})
    
    # 4. Interacting with functions from contract
    transaction = mvp_contract.setGreeting("hello world!", {"from": account})
    transaction.wait(1)

    greeting = mvp_contract.getGreeting()
    logger(f"getGreeting(): {greeting}")


def logger(message):
    print(f"[Logger] {message}")