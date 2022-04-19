# Brownie, on testnet
Reference video timestamp: https://youtu.be/M576WGiDBdQ?t=17967
Documentation: https://eth-brownie.readthedocs.io/en/stable/core-contracts.html#persisting-contracts-between-sessions

## What is this
How to get a deployed contract and interact with it with brownie + infura

## Prerequisites
1. Install dependencies
```bash
# https://eth-brownie.readthedocs.io/en/stable/install.html#installing-brownie
$ pipx install eth-brownie

# https://yarnpkg.com/package/ganache
$ yarn add -g ganache
```

2. Have an already deployed transaction. In this example, it'll be https://rinkeby.etherscan.io/tx/0x780d806a69ed3ad73de35f974728332d951586c4da25476fb2cfafbc1e1ffea1.

## Getting started
1. Initialize a new brownie project
```bash
$ brownie init
```

2. Create a solidity contract file in [./contracts/](./contracts/). 

## Compile contract
```bash
$ brownie compile
```

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

2. Specify to brownie we're using infura as web3 provider via environment variable. Add an environment variable named `WEB3_INFURA_PROJECT_ID` with value from infura's project id in [.env](.env) file. `WEB3_INFURA_PROJECT_ID` must be exact as it is a key. More info: https://eth-brownie.readthedocs.io/en/stable/network-management.html?highlight=infura#using-infura.

``` diff
+   export WEB3_INFURA_PROJECT_ID=xxxxxxxxxxxxxxxxxxxxxx

```
<p align="center">
<img src="https://i.ibb.co/gMvXcmK/untitled.png" width="500px">
</p>

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
2. Create a python script under [./scripts](./scripts). Example is in [./read_value_from_testnet_contract.py](./scripts/read_value_from_testnet_contract.py).

3. Run script, but specify `--network` param with `rinkeby` value, as that's the testnet we're deploying to. At the time of writing, this was the transaction: https://rinkeby.etherscan.io/address/0x9aCAb41b3729BE63e181625392bA8f95D0F2A5e1
```bash
$ brownie run scripts/read_value_from_testnet_contract.py --network rinkeby
    Brownie v1.18.1 - Python development framework for Ethereum

    MvpGetFromTestnetProject is the active project.

    Running 'scripts/read_value_from_testnet_contract.py::main'...
    Enter password for "dev_account1": 
    [Logger] old_greeting: goodbye, world
    Transaction sent: 0x06e3585b8ccf652cb6130b6455948bf328afa5fce387e9aac4077d33b32faff2
    Gas price: 1.000012883 gwei   Gas limit: 30549   Nonce: 34
    MVP.setGreeting confirmed   Block: 10410223   Gas used: 27772 (90.91%)

    [Logger] new_greeting: goodbye, world
```