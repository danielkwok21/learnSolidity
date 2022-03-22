import json
from web3 import Web3
from solcx import compile_standard, install_solc
import os
from dotenv import load_dotenv

load_dotenv()
install_solc("0.6.0")

# 1. Read contents of solidity file
with open("./mvp.sol", "r") as file:
    mvp_contents = file.read()

# 2. Compile solidity
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

# 2.1 Write compiled solidity to file for easy viewing
with open("compiled_code.json", "w") as file:
    json.dump(compiled_sol, file)

# 3. Get bytecode
bytecode = compiled_sol["contracts"]["mvp.sol"]["MVP"]["evm"]["bytecode"]["object"]

# 4. Get abi
abi = compiled_sol["contracts"]["mvp.sol"]["MVP"]["abi"]

# 5. Setting up ganache params
w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:7545"))
chain_id = 1337
my_address = "0x63094D96A0aCE0121a540ff680459e8233512727"
private_key = os.getenv("PRIVATE_KEY")

# 6. Creating contract
mvp_contract = w3.eth.contract(abi=abi, bytecode=bytecode)

# 7. Get number of transactions, put into nonce
nonce = w3.eth.getTransactionCount(my_address)

# 8. Create transaction
transaction = mvp_contract.constructor().buildTransaction({
    "gasPrice": w3.eth.gas_price, 
    "chainId": chain_id,
    "from": my_address,
    "nonce": nonce
})

# 9. Sign transaction
signed_transaction = w3.eth.account.sign_transaction(transaction, private_key=private_key)

# 10. Send transaction
transaction_hash = w3.eth.send_raw_transaction(signed_transaction.rawTransaction)

# 11. Wait for confirmation
transaction_receipt = w3.eth.wait_for_transaction_receipt(transaction_hash)

print(transaction_receipt)