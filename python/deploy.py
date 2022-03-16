import json
from web3 import Web3
from solcx import compile_standard, install_solc

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
my_address = "0x53b7C5d245480c8707EEB813Ec5ccb99dF20aDE1"
private_key = "0xba4429dc118e02de8c1f33851643694e431012290672fb0bb70ba95e3b9f4b53"

# 6. Creating contract
mvp_contract = w3.eth.contract(abi=abi, bytecode=bytecode)

# 7. Get number of transactions
nonce = w3.eth.getTransactionCount(my_address)

#8. Deploy contract
transaction = mvp_contract.constructor().buildTransaction({
    "gasPrice": w3.eth.gas_price, 
    "chainId": chain_id,
    "from": my_address,
    "nonce": nonce
})

print(transaction)