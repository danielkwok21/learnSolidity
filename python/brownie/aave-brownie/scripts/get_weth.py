from scripts.helpful_scripts import get_account
from brownie import interface, network, config
from web3 import Web3
import time

def main():
    get_weth()

def get_weth():
    account = get_account()
    amount = Web3.toWei(0.01, "ether")
  
    weth_address = config["networks"][network.show_active()]["weth_token"]
    weth = interface.IWeth(weth_address)
    tx = weth.deposit({"from": account, "value": amount})
    tx.wait(1)
    logger(f"Received 0.01 weth")

def logger(message):
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    print(f"[Logger {current_time}] {message}")