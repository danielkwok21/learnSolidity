# delete network

```bash
$ brownie networks delete mainnet-fork
    Brownie v1.18.1 - Python development framework for Ethereum

    SUCCESS: Network 'mainnet-fork' has been deleted
```
Development
  ├─Ganache-CLI: development
  ├─Geth Dev: geth-dev
  ├─Hardhat: hardhat
  ├─Hardhat (Mainnet Fork): hardhat-fork
  ├─Ganache-CLI (Mainnet Fork): mainnet-fork
  ├─Ganache-CLI (BSC-Mainnet Fork): bsc-main-fork
  ├─Ganache-CLI (FTM-Mainnet Fork): ftm-main-fork
  ├─Ganache-CLI (Polygon-Mainnet Fork): polygon-main-fork
  ├─Ganache-CLI (XDai-Mainnet Fork): xdai-main-fork
  ├─Ganache-CLI (Avax-Mainnet Fork): avax-main-fork
  └─Ganache-CLI (Aurora-Mainnet Fork): aurora-main-fork

# add network

```bash
$ brownie networks add development mainnet-fork cmd=ganache-cli host=http://127.0.0.1 fork=https://eth-rinkeby.alchemyapi.io/v2/jxBYZilUAWEmA4GBK0MAJEu4cEgw7zzm accounts=10 mnemonic=brownie port=8545

Brownie v1.18.1 - Python development framework for Ethereum

SUCCESS: A new network 'mainnet-fork' has been added
  └─mainnet-fork
    ├─id: mainnet-fork
    ├─cmd: ganache-cli
    ├─cmd_settings: {'fork': 'https://eth-rinkeby.alchemyapi.io/v2/jxBYZilUAWEmA4GBK0MAJEu4cEgw7zzm', 'accounts': 10, 'mnemonic': 'brownie', 'port': 8545}
    └─host: http://127.0.0.1
```