from scripts.helpful_scripts import get_account
from brownie import interface, network, config
from web3 import Web3
import time

def main():
    get_weth()

def get_weth():
    account = get_account()
    amount_in_eth = 0.01
    amount_in_wei = Web3.toWei(amount_in_eth, "ether")
  
    weth_address = config["networks"][network.show_active()]["weth_token"]
    weth = interface.IWeth(weth_address)
    tx = weth.deposit({"from": account, "value": amount_in_wei})
    tx.wait(1)
    logger(f"Received {amount_in_eth}wei of weth")

def logger(message):
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    print(f"[Logger {current_time}] {message}")