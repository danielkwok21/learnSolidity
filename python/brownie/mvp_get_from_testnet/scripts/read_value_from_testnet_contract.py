# 1. Import accounts and MVP from brownie
# accounts is the list of 10 dummy accounts provided by brownie
# MVP is an array of deployed solidity contract. MVP[-1] to get latest deployment
from brownie import accounts, MVP, Contract

def main():
    read_value_from_testnet_contract()


def read_value_from_testnet_contract():
    most_recent_deployment = MVP[-1]

    logger(most_recent_deployment.getGreeting())
    


def logger(message):
    print(f"[Logger] {message}")