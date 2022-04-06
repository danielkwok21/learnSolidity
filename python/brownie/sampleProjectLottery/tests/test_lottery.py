import time
from brownie import accounts, Lottery
from web3 import Web3

def testGetEntraceFeeInWei():
    account = accounts[0]

    Lottery_contract = Lottery.deploy({"from": account})

    entranceFeeInWei = Lottery_contract.getEntraceFeeInWei()

    logger(f"entranceFeeInWei: {entranceFeeInWei}")
 
    # 6 April 2022 0.01494375171
    assert entranceFeeInWei > Web3.toWei(0.014, "ether")
    assert entranceFeeInWei < Web3.toWei(0.015, "ether")

def logger(message):
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    print(f"[Logger {current_time}] {message}")