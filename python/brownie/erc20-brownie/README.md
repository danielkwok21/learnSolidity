# Creating & deploying ERC20 token
Video: https://youtu.be/M576WGiDBdQ?t=30192

## What is this
How to create & deploy a token with ERC20 standard.

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
5. In [.env](.env) file, specify `PRIVATE_KEY` with value metamask account's private key. This allows us to deploy to token using our account
```diff
    export GITHUB_TOKEN=xxxxxxxxxxxxxxxxxxxxxx
    export WEB3_INFURA_PROJECT_ID=xxxxxx
+   export PRIVATE_KEY=xxxxxx
```

## Installing dependencies
For this example, we'll be installing chainlink and openzeppline as dependencies.

1. Install with `brownie pm install <ORGANIZATION>/<REPOSITORY>@<VERSION>`
```console
$ brownie pm install smartcontractkit/chainlink@1.2.1

$ brownie pm install OpenZeppelin/openzeppelin-contracts@4.5.0
```

2. Verify installation with `brownie pm list`
```console
$ brownie pm list
  
Brownie v1.18.1 - Python development framework for Ethereum
The following packages are currently installed:
smartcontractkit
 └─smartcontractkit/chainlink@1.2.1
OpenZeppelin
 └─OpenZeppelin/openzeppelin-contracts@4.5.0
```

3. Specify dependency usage at [./brownie-config.yml](./brownie-config.yml)
```diff
    dotenv: .env
+   dependencies:
+  - smartcontractkit/chainlink@1.2.1
+  - OpenZeppelin/openzeppelin-contracts@4.5.0
```

## Deploy
1. Create a python script under [./scripts](./scripts). Example is in [./deploy.py](./scripts/deploy.py). We've also created a [helpful_scripts.py](./scripts/helpful_scripts.py) that contains util functions for deployments.

2. Deploy locally to test
```console
$ brownie run scripts/deploy.py

Brownie v1.18.1 - Python development framework for Ethereum
Erc20BrownieProject is the active project.

Launching 'ganache-cli --chain.vmErrorsOnRPCResponse true --wallet.totalAccounts 10 --hardfork istanbul --miner.blockGasLimit 12000000 --wallet.mnemonic brownie --server.port 8545'...

Running 'scripts/deploy.py::main'...
Transaction sent: 0xb58fdb9912c8f7f5792acc1797da38615e608f7ded2605930394cdb92b8d3fed
  Gas price: 0.0 gwei   Gas limit: 12000000   Nonce: 0
  OurToken.constructor confirmed   Block: 1   Gas used: 636800 (5.31%)
  OurToken deployed at: 0x3194cBDC3dbcd3E11a07892e7bA5c3394048Cc87

[Logger 10:46:19] contract name: OurToken
Terminating local RPC client...
```

3. Deploy to testnet by specifying `--network` param with `rinkeby` value, as that's the testnet we're deploying to.
At the time of writing, this contract was deployed to https://rinkeby.etherscan.io/address/0x9C4168402b28e9349ac072f2310427923EbDf8f3

```console
$ brownie run scripts/deploy.py --network rinkeby
```
