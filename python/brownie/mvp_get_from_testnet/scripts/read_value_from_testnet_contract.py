from brownie import accounts, MVP, Contract


def main():
    read_value_from_testnet_contract()


def read_value_from_testnet_contract():
    # Where is "dev_account1" coming from?
    # Make sure to read through README#deploy-contract-to-test-net-with-own-account first
    account = accounts.load("dev_account1")

    most_recent_deployment = Contract("0x9aCAb41b3729BE63e181625392bA8f95D0F2A5e1")

    old_greeting = most_recent_deployment.getGreeting()
    logger("old_greeting: "+old_greeting)

    most_recent_deployment.setGreeting("goodbye, world", {"from": account})

    new_greeting = most_recent_deployment.getGreeting()
    logger("new_greeting: "+new_greeting)


def logger(message):
    print(f"[Logger] {message}")
