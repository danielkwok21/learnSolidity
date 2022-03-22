# 1. Import accounts and MVP from brownie
# accounts is the list of 10 dummy accounts provided by brownie
# MVP is an array of deployed solidity contract. MVP[-1] to get latest deployment
from brownie import accounts, MVP

def main():
    deploy_local_with_own_account()


def deploy_local_with_own_account():
    # Where is "dev_account1" coming from?
    # Make sure to read through README#deploy-contract-to-test-net-with-own-account first
    account = accounts.load("dev_account1")
    print(f"Account selected: {account}")
    
    # 3. Deploy solidity contract
    mvp_contract = MVP.deploy({"from": account})
    
    # 4. Interacting with functions from contract
    transaction = mvp_contract.setGreeting("hello world!", {"from": account})
    transaction.wait(1)

    greeting = mvp_contract.getGreeting()
    logger(f"getGreeting(): {greeting}")


def logger(message):
    print(f"[Logger] {message}")