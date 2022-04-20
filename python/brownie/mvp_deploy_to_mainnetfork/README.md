# Brownie, on forked network
Reference video timestamp: https://youtu.be/M576WGiDBdQ?t=21287

## What is this
How to deploy a contract to a forked network

## Why do we do this?
A mainnet-fork is like a copy of a real deployed blockchain, e.g. rinkeby, ethereum, etc. We use a service called [Alchemy](https://www.alchemy.com/) for this.

There is a default forked Ethereum network called `mainnet-fork` already provided by brownie, but there're issues with it. So this is why we're doing it ourselves.

## Prerequisites
1. Install dependencies
```bash
# https://eth-brownie.readthedocs.io/en/stable/install.html#installing-brownie
$ pipx install eth-brownie

# https://yarnpkg.com/package/ganache
$ yarn add -g ganache
```

2. Have an alchemy account. https://www.alchemy.com/

3. Have a dummy solidity contract file in [./contracts/](./contracts/). 


## Adding a new network on brownie
1. Run command to add network. Remember to provide alchemy project id for parameter `fork`. 
Key params include:
- `mainnet-fork-dev` as the id
- to create 10 `accounts`


More details at https://eth-brownie.readthedocs.io/en/stable/network-management.html#adding-a-new-network


```bash
$ brownie networks add development mainnet-fork-dev cmd=ganache-cli host=http://127.0.0.1 fork='https://eth-mainnet.alchemyapi.io/v2/<INSERT-ALCHEMY-PROJECT-ID-HERE>' accounts=10 mnemonic=brownie port=8545
```

2. Verify with `$ brownie networks list`. Should be able to see our newly created network `mainnet-fork-dev`
```bash
Development
...
└─mainnet-fork-dev: mainnet-fork-dev
```

3. Verify again by trying to start a console with `$ brownie console --network mainnet-fork-dev`

## Deploy to forked network
1. Run `$ brownie run scripts/deploy.py --network mainnet-fork-dev`
```bash
Brownie v1.18.1 - Python development framework for Ethereum

MvpDeployToMainnetforkProject is the active project.

Launching 'ganache-cli --chain.vmErrorsOnRPCResponse true --wallet.totalAccounts 10 --fork.url https://eth-mainnet.alchemyapi.io/v2/JdZ0wCrRKW35uVyocix2HijVLnsiIb2Q --wallet.mnemonic brownie --server.port 8545 --hardfork istanbul'...

Running 'scripts/deploy.py::main'...
Account selected: 0x66aB6D9362d4F35596279692F0251Db635165871
Transaction sent: 0xee7ec19e76898bf3dc13aa75cde7cd953f23605a4a922473f4898dc4dd7c75fe
  Gas price: 0.0 gwei   Gas limit: 30000000   Nonce: 2
  MVP.constructor confirmed   Block: 14620758   Gas used: 277035 (0.92%)
  MVP deployed at: 0xE7eD6747FaC5360f88a2EFC03E00d25789F69291

Transaction sent: 0xc6399fa0b547c84f7de6a22ce06a657843fd7c481a0afb6dbf72ad63a5e21f6f
  Gas price: 0.0 gwei   Gas limit: 30000000   Nonce: 3
  MVP.setGreeting confirmed   Block: 14620759   Gas used: 45499 (0.15%)

  MVP.setGreeting confirmed   Block: 14620759   Gas used: 45499 (0.15%)

[Logger 16:14:55] getGreeting(): hello world!
Terminating local RPC client...
```