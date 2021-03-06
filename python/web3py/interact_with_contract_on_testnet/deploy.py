import json
from web3 import Web3
from solcx import compile_standard, install_solc
import os
from dotenv import load_dotenv

load_dotenv()
install_solc("0.6.0")

with open("./mvp.sol", "r") as file:
    mvp_contents = file.read()

# compile
compiled_sol = compile_standard(
    {
        "language": "Solidity",
        "sources": {
            "mvp.sol": {
                "content": mvp_contents
            }
        },
        "settings": {
            "outputSelection": {
                "*": {
                    "*": ["abi", "metadata", "evm.bytecode", "evm.bytecode.sourceMap"]
                }
            }
        },
    },
    solc_version="0.6.0"
)
with open("compiled_code.json", "w") as file:
    json.dump(compiled_sol, file)
print("Compiling...")

# get bytecode & abi
bytecode = compiled_sol["contracts"]["mvp.sol"]["MVP"]["evm"]["bytecode"]["object"]
abi = compiled_sol["contracts"]["mvp.sol"]["MVP"]["abi"]

# ganache params
w3 = Web3(Web3.HTTPProvider(os.getenv("RINKEBY_ENDPOINT"))) 
chain_id = 4 # get chain_id from https://chainlist.org/ (e.g. rinkeby chainid = 4)
my_address = os.getenv("PUBLIC_KEY")
private_key = os.getenv("PRIVATE_KEY")

# create transaction
mvp_contract = w3.eth.contract(abi=abi, bytecode=bytecode)
nonce = w3.eth.getTransactionCount(my_address)
transaction = mvp_contract.constructor().buildTransaction({
    "gasPrice": w3.eth.gas_price, 
    "chainId": chain_id,
    "from": my_address,
    "nonce": nonce
})
print("Deploying...")

# sign transaction
signed_transaction = w3.eth.account.sign_transaction(transaction, private_key=private_key)
# send transaction
transaction_hash = w3.eth.send_raw_transaction(signed_transaction.rawTransaction)
# get transaction receipt
transaction_receipt = w3.eth.wait_for_transaction_receipt(transaction_hash)

print("...deployed")

# 1. Find contract from transaction
mvp_contract = w3.eth.contract(address=transaction_receipt.contractAddress, abi=abi)

# call() is simulate calling a function, without making a state change.
# the following line of code has no write effect on the blockchain
mvp_contract.functions.setGreeting("hello world").call()

print("setGreeting()...")

# 2. Invoke "setGreeting" function from contract
# buildTransaction() is calling a function to actually make a state change
# "nonce" here is "nonce+1" because nonce is unique per transaction. The previous value of "nonce" is used when building the original contract
setgreeting_transaction = mvp_contract.functions.setGreeting("hello world").buildTransaction({
    "gasPrice": w3.eth.gas_price, 
    "chainId": chain_id,
    "from": my_address,
    "nonce": nonce+1
})

# 2.1 sign, send, wait 
signed_setgreeting_transaction = w3.eth.account.sign_transaction(setgreeting_transaction, private_key=private_key)
setgreeting_transaction_hash = w3.eth.send_raw_transaction(signed_setgreeting_transaction.rawTransaction)
setgreeting_transaction_receipt = w3.eth.wait_for_transaction_receipt(setgreeting_transaction_hash)

print("...setGreeting() done")

# 3.1 Invoke "getGreeting" function from contract
greeting = mvp_contract.functions.getGreeting().call()
print("Updated greeting: "+greeting)