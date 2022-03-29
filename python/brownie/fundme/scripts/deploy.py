from brownie import FundMe, accounts


def main():
    deploy()


def deploy():
    account = accounts.load("dev_account1")
    # publish_source=True
    # This is a flag to publish source code
    # to testnet
    fund_me_contract = FundMe.deploy({"from": account}, publish_source=True)