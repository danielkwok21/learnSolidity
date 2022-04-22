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


## Run on mainnet fork
Keep in mind `mainnet-fork-dev` is our personally forked mainnet. Refer to [mvp_deploy_to_forked_network](../mvp_deploy_to_forked_network/).

No need to run [scripts/get_weth.py](./scripts/get_weth.py) as there is no way to get weth for an account before hand, as accounts are generated on-the-fly in mainnet-fork-dev


Simply run [scripts/aave_borrow.py](./scripts/aave_borrow.py). Details of what's happening is in the script. 
```bash
$ brownie run scripts/aave_borrow.py --network mainnet-fork-dev
```


## Run on kovan
All following operation takes place in real, live, Kovan testnet. Hence all operations can be observed from etherscan, metamask, and aave itself.

Kovan etherscan - https://kovan.etherscan.io/

AAVE - https://staging.aave.com/?marketName=proto_kovan

1. Convert some eth into weth. Observe decrease in ETH and increase in WETH.
```bash
$ brownie run scripts/get_weth.py --network kovan
```
Before:

<img loading="lazy" src="https://i.ibb.co/7pQtNyw/1.png" width=600>

After: 

<img loading="lazy" src="https://i.ibb.co/qrjqfCs/2.png" width=600 >

2. Run [./scripts/aave_borrow.py](./scripts/aave_borrow.py) script. Details of what's happening is in the script. Observe dercrease in WETH and increase in DAI

```bash
$ brownie run scripts/aave_borrow.py --network kovan
```

Before:

<img loading="lazy" src="https://i.ibb.co/qrjqfCs/2.png" width=600 >

After:

<img loading="lazy" src="https://i.ibb.co/sQKydcF/3.png" width=600>

## FAQ
Q: How to repay all borrowed tokens?

A: Head to https://staging.aave.com/?marketName=proto_kovan. Click "Repay" on borrowed asset.

<img loading="lazy" src="https://i.ibb.co/bRtJ9FB/Whats-App-Image-2022-04-22-at-5-18-43-PM.jpg" width=600>