# Interact with contract on testnet
Reference video timestamp: https://youtu.be/M576WGiDBdQ?t=15780

## What is this
How to deploy to testnet (using Infura)
<br />How to interact with a deployed contract using python.
<br />This code is built on top of [../interact_with_contract](../interact_with_contract/).


## Prerequisites
1. Install dependencies
```bash
# https://web3py.readthedocs.io/en/stable/quickstart.html#installation
$ pip3 install web3

# https://pypi.org/project/python-dotenv/
$ pip3 install python-dotenv

# https://pypi.org/project/py-solc-x/
$ pip3 install py-solc-x
```

2. Sign up for infura (or any web3 provider)
    
    https://infura.io/

## Getting started
1. Setup an infura project. \
Set "ENDPOINTS" to `RINKEBY`
![https://i.ibb.co/zbgbxdG/untitled.png](https://i.ibb.co/zbgbxdG/untitled.png)

2. Pick an account from metamask. This'll be used for the subsequent steps

3. Set required environment variables in [.env](./.env)
```
// .env
export PUBLIC_KEY=<insert-metamask-account-public-key-here>
export PRIVATE_KEY=<insert-metamask-account-private-key-here>

# update with ENDPOINT (https, not wss) copied from infura
export RINKEBY_ENDPOINT=https://rinkeby.infura.io/xxxxxxxxxxx
```

4. Run deploy.py
```bash
$ python3 deploy.py
```

5. Wait for transactions to be completed in terminal
``` bash
Compiling...
Deploying...
...deployed
setGreeting()...
...setGreeting() done
Updated greeting: hello world
```

6. Wait a couple minutes before going on etherscan rinkeby (https://rinkeby.etherscan.io)

7. Search the address used in the env var `PUBLIC_KEY`

8. View transaction
![https://i.ibb.co/sVN3TFw/untitled-1.png](https://i.ibb.co/sVN3TFw/untitled-1.png)