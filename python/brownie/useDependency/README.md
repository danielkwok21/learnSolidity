# Using dependency in brownie
Reference doc: 
https://eth-brownie.readthedocs.io/en/stable/package-manager.html

## What is this
How to install & use dependencies with brownie.

## Caveats
In eth, dependencies are usually other contracts.
This means our contract must be deployed to either testnets or mainnets to have access to these contracts.

## Prerequisites
### Environment variables
1. Specify at [./brownie-config.yml](./brownie-config.yml) to allow for env files. This'll be used at the following steps.
```diff
+   dotenv: .env
```

2. Create [.env](.env) file

2. In [.env](.env) file, specify `GITHUB_TOKEN` with value from github personal access token.https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token. This allows us to install dependencies from github. `GITHUB_TOKEN` must be exact as it is a key.
```diff
+   export GITHUB_TOKEN=xxxxxxxxxxxxxxxxxxxxxx
```

3. In [.env](.env) file, specify `WEB3_INFURA_PROJECT_ID` with value from infura. This allows us to deploy contract to testnet via Infura. Feel free to use other web3 providers. `WEB3_INFURA_PROJECT_ID` must be exact as it is a key.
```diff
    export GITHUB_TOKEN=xxxxxxxxxxxxxxxxxxxxxx
+   export WEB3_INFURA_PROJECT_ID=xxxxxx
```

4. Validate infura is connected via `$ brownie networks list`. Should be able to see networks labeled "Infura"
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

### Importing account
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

## Installing dependencies
For this example, we'll be installing chainlink as a dependency. https://docs.chain.link/docs/get-the-latest-price/#solidity.

1. Install with `brownie pm install <ORGANIZATION>/<REPOSITORY>@<VERSION>`
```console
$ brownie pm install smartcontractkit/chainlink@1.2.1

Brownie v1.18.1 - Python development framework for Ethereum
16.3MiB [00:58, 280kiB/s] 
WARNING: Unable to compile smartcontractkit/chainlink@1.2.1 due to a NamespaceCollision - you may still be able to import sources from the package, but will be unable to load the package directly.

SUCCESS: Package 'smartcontractkit/chainlink@1.2.1' has been installed
```

2. Verify installation with `brownie pm list`
```console
$ brownie pm list
  
Brownie v1.18.1 - Python development framework for Ethereum
The following packages are currently installed:
smartcontractkit
└─smartcontractkit/chainlink@1.2.1
```

3. Specify dependency usage at [./brownie-config.yml](./brownie-config.yml)
```diff
    dotenv: .env
+   dependencies:
+     - smartcontractkit/chainlink@1.2.1
```

## Deploy

2. Create a python script under [./scripts](./scripts). Example is in [./deploy.py](./scripts/deploy.py).

3. Run script, but specify `--network` param with `rinkeby` value, as that's the testnet we're deploying to.
```console
$ brownie run scripts/deploy.py --network rinkeby

Brownie v1.18.1 - Python development framework for Ethereum

Compiling contracts...
Solc version: 0.8.13
Optimizer: Enabled  Runs: 200
EVM Version: Istanbul
Generating build data...
- smartcontractkit/chainlink@1.2.1/AggregatorV3Interface
- ConvertEthToUsd

UsedependencyProject is the active project.

Running 'scripts/deploy.py::main'...
Enter password for "dev_account1": 
Account selected: 0x71Ef85Af03fC61Ad0c69Bd5bc8D16ca2dB27E9a4
Transaction sent: 0x66d870a2ab66e1e58e32c43b00be309965f85a723af6b7b45ec2acf734442b71
Gas price: 1.000000009 gwei   Gas limit: 190692   Nonce: 37
ConvertEthToUsd.constructor confirmed   Block: 10420405   Gas used: 173357 (90.91%)
ConvertEthToUsd deployed at: 0xCf47a4BC80Ed4E4f51a2FE83B6928B39c5043773

[Logger 11:05:28] Latest price in usd: 3408
```