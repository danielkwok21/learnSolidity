# 1. Import accounts and MVP from brownie
# accounts is the list of 10 dummy accounts provided by brownie
# MVP is an array of deployed solidity contract. MVP[-1] to get latest deployment
from brownie import accounts, MVP
import time

def main():
    deploy_mainnet_fork()


def deploy_mainnet_fork():
    account = accounts[0]
    print(f"Account selected: {account}")
    
    # 3. Deploy solidity contract
    mvp_contract = MVP.deploy({"from": account})
    
    # 4. Interacting with functions from contract
    transaction = mvp_contract.setGreeting("hello world!", {"from": account})
    transaction.wait(1)

    greeting = mvp_contract.getGreeting()
    logger(f"getGreeting(): {greeting}")

def logger(message):
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    print(f"[Logger {current_time}] {message}")