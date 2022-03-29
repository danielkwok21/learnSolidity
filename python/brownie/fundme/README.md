# Brownie + payable contracts
Reference video timestamp: https://youtu.be/M576WGiDBdQ?t=18384

## What is this
How to write fundable contracts in brownie
How to publish sourcecode to testnet


## Prerequisites
```bash
# https://eth-brownie.readthedocs.io/en/stable/install.html#installing-brownie
$ pipx install eth-brownie

# https://yarnpkg.com/package/ganache
$ yarn add -g ganache
```

## Getting started
1. Initialize a new brownie project
```bash
$ brownie init
```

2. Create a solidity contract file in [./contracts/](./contracts/). 

<br />

## Deploy contract to test net with own account

1. Import account via private key with `$ brownie accounts new <insert-account-name>`
```bash
# Create a new brownie account via existing private key
$ brownie accounts new dev_account1

    Brownie v1.18.1 - Python development framework for Ethereum

    Enter the private key you wish to add: xxxxxxxxxxxxxxxxxxxxxxxxxxxx
    Enter the password to encrypt this account with: 
    SUCCESS: A new account '0x71Ef85Af03fC61Ad0c69Bd5bc8D16ca2dB27E9a4' has been generated with the id 'dev_account1'

# Verify account creation
$ brownie accounts list

    Brownie v1.18.1 - Python development framework for Ethereum

    Found 1 account:
    └─dev_account1: 0x71Ef85Af03fC61Ad0c69Bd5bc8D16ca2dB27E9a4
```

2. Create [brownie-config.yaml](./brownie-config.yaml) as such to point brownie where to get environment variables from.
```diff
+   dotenv: .env
```

2. Specify to brownie we're using infura as web3 provider via environment variable. Add an environment variable named `WEB3_INFURA_PROJECT_ID` with value from infura's project id in [.env](.env) file. `WEB3_INFURA_PROJECT_ID` must be exact as it is a key.
``` diff
+   export WEB3_INFURA_PROJECT_ID=xxxxxxxxxxxxxxxxxxxxxx

```
<img src="https://i.ibb.co/gMvXcmK/untitled.png" width="500px">


3. Validate infura is connected via `$ brownie networks list`. Should be able to see networks labeled "Infura"
```bash
$ brownie networks list
    Brownie v1.18.1 - Python development framework for Ethereum

    The following networks are declared:

    Ethereum
    ├─Mainnet (Infura): mainnet
    ├─Ropsten (Infura): ropsten
    ├─Rinkeby (Infura): rinkeby 
    ├─Goerli (Infura): goerli
    └─Kovan (Infura): kovan
```
4. Specify to brownie api key from etherscan. This allows brownie to auto upload sourcecode to testnet when it's deployed. `ETHERSCAN_TOKEN` must be exactly as it is a key.
``` diff
    export WEB3_INFURA_PROJECT_ID=xxxxxxxxxxxxxxxxxxxxxx
+   export ETHERSCAN_TOKEN=xxxxxxxxxxxxxxxxxxxxxx

```

5. Create a python deployment script under [./scripts](./scripts). Example is in [./deploy.py](./scripts/deploy.py).

6. Run script, but specify `--network` param with `rinkeby` value, as that's the testnet we're deploying to. 
```bash
$ brownie run scripts/deploy.py --network rinkeby

  Brownie v1.18.1 - Python development framework for Ethereum

    FundmeProject is the active project.

    Running 'scripts/deploy.py::main'...
    Enter password for "dev_account1": 
    Transaction sent: 0x4bfca381a34af86fa05f65492f686914390148b63436455b0a87066f1d59b203
    Gas price: 1.000000023 gwei   Gas limit: 175145   Nonce: 31
    FundMe.constructor confirmed   Block: 10409849   Gas used: 159223 (90.91%)
    FundMe deployed at: 0x5DF6Bc02fc665c338cC91d50Aad7Bde5ee89D9d0

    Waiting for https://api-rinkeby.etherscan.io/api to process contract...
    Verification submitted successfully. Waiting for result...
    Verification pending...
    Verification complete. Result: Already Verified
```

7. View code at https://rinkeby.etherscan.io/address/0x5DF6Bc02fc665c338cC91d50Aad7Bde5ee89D9d0#code
![https://i.ibb.co/yR44rNT/Whats-App-Image-2022-03-29-at-15-07-58.jpg](https://i.ibb.co/yR44rNT/Whats-App-Image-2022-03-29-at-15-07-58.jpg)