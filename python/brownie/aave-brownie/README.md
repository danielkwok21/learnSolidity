# Interacting with AAVE using brownie
Video: https://youtu.be/M576WGiDBdQ?t=31685

## What is this
Interacting with aave with a list of actions
1. Deposit some eth into aave
2. Borrow some asset with ETH collateral
3. Repay everything

## Prerequisites
1. Uses kovan test net, i.e. need credits in account in kovan


## Steps
### Setting up WETH contract

- Doc at https://docs.aave.com/developers/v/2.0/the-core-protocol/weth-gateway
- Interface source codes at https://github.com/aave/protocol-v2/blob/master/contracts/misc
- AAVE contract addresses at https://docs.aave.com/developers/v/2.0/deployed-contracts/deployed-contracts

1. Create [IWeth.sol](./interfaces/IWeth.sol) under [interfaces](./interfaces/) according to interface specifed in https://github.com/PatrickAlphaC/aave_brownie_py/blob/main/interfaces/WethInterface.sol (Where did PatrickAlphaC got this interface from?)

2. Specify kovan's WETH token's address in [brownie-config.yaml](./brownie-config.yaml) based on https://kovan.etherscan.io/token/0xd0a1e359811322d97991e03f863a0c30c2cf029c

    brownie-config.yaml
    ```diff
    +   networks:
    +       kovan:
    +           weth_token: '0xd0a1e359811322d97991e03f863a0c30c2cf029c'
    ```

3. Specify mainnet's WETH token's address in [brownie-config.yaml](./brownie-config.yaml) based on https://etherscan.io/token/0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2 (will be useful when testing in mainnet fork)

    brownie-config.yaml
    ```diff
    networks:
        kovan:
            weth_token: '0xd0a1e359811322d97991e03f863a0c30c2cf029c'
    +   mainnet-fork:
    +       weth_token: + '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2'

    ```

### Additional configs

1. Specify wallet address, to interact with aave with our account's contract

    brownie-config.yaml
    ```diff
    networks:
    kovan:
        weth_token: '0xd0a1e359811322d97991e03f863a0c30c2cf029c'
    +   wallets:
    +       from_key: ${PRIVATE_KEY}

    ```

## Deploy on kovan
```bash
$ brownie run scripts/get_weth.py --network kovan

Brownie v1.18.1 - Python development framework for Ethereum

AaveBrownieProject is the active project.

Running 'scripts/get_weth.py::main'...
Transaction sent: 0xf9c0f7c9dbdb4098412b4fefeb2b879936efadb57e4ecd9353851ebef2cde69d
  Gas price: 2.500000007 gwei   Gas limit: 49572   Nonce: 0
  Transaction confirmed   Block: 31124816   Gas used: 45066 (90.91%)

[Logger 09:54:56] Received 0.01 weth

```
<img src="https://i.ibb.co/qR1g77x/untitled.png" height=200 >
(Need to import WETH token beforehand)

## Deploy on mainnet fork
Keep in mind `mainnet-fork-dev` is our personally forked mainnet. Refer to [mvp_deploy_to_forked_network](../mvp_deploy_to_forked_network/)
```bash
$ brownie run scripts/aave_borrow.py --network mainnet-fork-dev

Brownie v1.18.1 - Python development framework for Ethereum

AaveBrownieProject is the active project.

Launching 'ganache-cli --chain.vmErrorsOnRPCResponse true --wallet.totalAccounts 10 --fork.url https://eth-mainnet.alchemyapi.io/v2/JdZ0wCrRKW35uVyocix2HijVLnsiIb2Q --wallet.mnemonic brownie --server.port 8545 --hardfork istanbul'...

Running 'scripts/aave_borrow.py::main'...
Transaction sent: 0xc6e2d2fa462aa8886da9bc132d031a6fdf4eab81b02b87aaf413b89ccdef8bd7
  Gas price: 0.0 gwei   Gas limit: 30000000   Nonce: 2
  Transaction confirmed   Block: 14621001   Gas used: 43738 (0.15%)

  Transaction confirmed   Block: 14621001   Gas used: 43738 (0.15%)

[Logger 17:07:44] Received 0.01 weth
Terminating local RPC client...

```