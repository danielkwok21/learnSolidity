# 1. Import accounts and MVP from brownie
# accounts is the list of 10 dummy accounts provided by brownie
# MVP is an array of deployed solidity contract. MVP[-1] to get latest deployment
from brownie import accounts, MVP, Contract


def main():
    read_value_from_testnet_contract()


def read_value_from_testnet_contract():
    # Where is "dev_account1" coming from?
    # Make sure to read through README#deploy-contract-to-test-net-with-own-account first
    account = accounts.load("dev_account1")

    most_recent_deployment = MVP[-1]

    old_greeting = most_recent_deployment.getGreeting()
    logger("old_greeting: "+old_greeting)

    most_recent_deployment.setGreeting("goodbye, world", {"from": account})

    new_greeting = most_recent_deployment.getGreeting()
    logger("new_greeting: "+new_greeting)


def logger(message):
    print(f"[Logger] {message}")
