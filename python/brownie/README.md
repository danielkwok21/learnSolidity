# Interact with contract
Reference video timestamp: https://youtu.be/M576WGiDBdQ?t=16101

## What is this
How to build, deploy, and interact with contract using brownie.


## Prerequisites
```bash
# https://eth-brownie.readthedocs.io/en/stable/install.html#installing-brownie
$ pipx install eth-brownie

# https://yarnpkg.com/package/ganache
$ yarn add -g ganache
```

## Getting started
1. Initialize a new brownie project in a new directory called "mvp" and cd into it
```bash
$ brownie init mvp
$ cd mvp
```

2. Create a solidity contract file in [./mvp/contracts/](./mvp/contracts/). 

## Compile contract
```bash
$ brownie compile
```

## Deploy contract to local with dummy account

1. Create a python deployment script under [./mvp/scripts](./mvp/scripts). Details on file is in [./mvp/scripts/deploy_w_dummy_account.py](./mvp/scripts/deploy_w_dummy_account.py).

3. Run script
```bash
$ brownie run scripts/deploy_w_dummy_account.py
```


## Deploy contract to local with own account

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

2. Create a python deployment script under [./mvp/scripts](./mvp/scripts). Details on file is in [./mvp/scripts/deploy_w_own_account.py](./mvp/scripts/deploy_w_own_account.py).

3. Run script
```bash
$ brownie run scripts/deploy_w_own_account.py
```

## Testing
1. Write tests in [./mvp/tests/](./mvp/tests/).
2. Test file must be named test_*.py. E.g. test_mvp.py, test_blablabla.py
3. Run test with
```bash
# Run all test
$ brownie test

# Run a particular test case only
# $ brownie test -k <test-name>
$ brownie test -k test_default_value()
```