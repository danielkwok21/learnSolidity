# Interacting with AAVE using brownie
Video timestamp: https://youtu.be/M576WGiDBdQ?t=31685

## What is this
Interacting with aave with a list of actions
0. Convert some ethereum into weth
1. Deposit weth into aave
2. Borrow dei with depositted weth
3. Repay everything

## Prerequisites
1. Uses kovan testnet. Would need credits in account in kovan.
2. Import WETH and DAI token into acccount in kovan. This would allow us to view changes from metamask directly, rather than having to go to etherscan.

<!-- <img src="https://i.ibb.co/hX09TPJ/Whats-App-Image-2022-04-22-at-11-18-10-AM.jpg" height=400> -->


## Steps
Follow video. Too lengthy to add into readme.

## Important files and directories
[./scripts/aave_borrow.py](./scripts/aave_borrow.py)
- Main focus of this project

[./brownie-config.yaml](./brownie-config.yaml)

- Storing configurations. Specifically network-specific addresses, and wallet address

[./interfaces](./interfaces/)
- To interact with deployed contracts, we need interface + address. Here is where we store the interfaces.

[./contracts](./contracts/)
- Unlike previos projects, all contracts used here are already deployed. So this directory will be empty

[./scripts](./scripts)
- get_weth.py provides weth to specified account
- aave_borrow.py is the main focus of this project


## Run on kovan
1. Convert some eth into weth
```bash
$ brownie run scripts/get_weth.py --network kovan
```
Before:

<img loading="lazy" src="https://i.ibb.co/qpTmSGm/Whats-App-Image-2022-04-22-at-1-06-48-PM.jpg" width=300>

After: 

<img loading="lazy" src="https://i.ibb.co/nBNBC09/Whats-App-Image-2022-04-22-at-1-07-13-PM.jpg" width=300 >

2. Comment out `repay` function call in [./scripts/aave_borrow.py](./scripts/aave_borrow.py) to avoid repaying, so we can see the difference in account balance.

```diff
# scripts/aave_borrow.py
-   # 7. Repay all we've borrowed
-   #    Comment this out to see difference in value, else it'll go back to the previous value.
-    repay(borrowable_dai_in_wei, lending_pool, dai_addr, account)

+    # # 7. Repay all we've borrowed
+    # #    Comment this out to see difference in value, else it'll go back to the previous value.
+    # repay(borrowable_dai_in_wei, lending_pool, dai_addr, account)


```

3. Run [./scripts/aave_borrow.py](./scripts/aave_borrow.py) script. Details of what's happening is in the script.
```bash
$ brownie run scripts/aave_borrow.py --network kovan
```

Before:

<img loading="lazy" src="https://i.ibb.co/nBNBC09/Whats-App-Image-2022-04-22-at-1-07-13-PM.jpg" width=300 >

After:





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