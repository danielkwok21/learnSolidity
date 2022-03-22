# Brownie, on testnet
Reference video timestamp: https://www.youtube.com/watch?t=17624&v=M576WGiDBdQ&feature=youtu.be&ab_channel=freeCodeCamp.org

## What is this
How to build, deploy, and interact with contract on testnet using brownie + infura.

This example is built on top of [../mvp_deploy_to_local/](../mvp_deploy_to_local/)

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
2. Create a python deployment script under [./scripts](./scripts). Example is in [./deploy.py](./scripts/deploy.py).

3. Run script, but specify `--network` param with `rinkeby` value, as that's the testnet we're deploying to. At the time of writing, this was the transaction: https://rinkeby.etherscan.io/tx/0x780d806a69ed3ad73de35f974728332d951586c4da25476fb2cfafbc1e1ffea1
```bash
$ brownie run scripts/deploy.py --network rinkeby

    Brownie v1.18.1 - Python development framework for Ethereum

    MvpTestnetProject is the active project.

    Running 'scripts/deploy.py::main'...
    Enter password for "dev_account1": 
    Account selected: 0x71Ef85Af03fC61Ad0c69Bd5bc8D16ca2dB27E9a4
    Transaction sent: 0xf1d8c7f529adb1d5039e342022481b834f0d8ae5973b82d1fecaf8e40ed1053e
    Gas price: 1.000000073 gwei   Gas limit: 304738   Nonce: 27
    MVP.constructor confirmed   Block: 10365767   Gas used: 277035 (90.91%)
    MVP deployed at: 0x9aCAb41b3729BE63e181625392bA8f95D0F2A5e1

    Transaction sent: 0x780d806a69ed3ad73de35f974728332d951586c4da25476fb2cfafbc1e1ffea1
    Gas price: 1.000000073 gwei   Gas limit: 49938   Nonce: 28
    MVP.setGreeting confirmed   Block: 10365768   Gas used: 45399 (90.91%)

    MVP.setGreeting confirmed   Block: 10365768   Gas used: 45399 (90.91%)

    [Logger] getGreeting(): hello world!
```

## Testing
1. Write tests in [./tests/](./tests/).
2. Test file must be named test_*.py. E.g. test_mvp.py, test_blablabla.py
3. Run test with
```bash
# Run all test
$ brownie test

# Run a particular test case only
# $ brownie test -k <test-name>
$ brownie test -k test_deploy()
```