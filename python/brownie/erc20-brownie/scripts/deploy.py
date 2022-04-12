from brownie import OurToken
from web3 import Web3
import time
from scripts.helpful_scripts import get_account

initial_supply = Web3.toWei(1000, 'ether')

def main():
    deploy()

def deploy():
    account = get_account()
    our_token_contract = OurToken.deploy(initial_supply,{"from":account})
    logger(f"contract name: {our_token_contract.name()}")


def logger(message):
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    print(f"[Logger {current_time}] {message}")