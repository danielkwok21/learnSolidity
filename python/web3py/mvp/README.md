# MVP
Reference video timestamp:  https://youtu.be/M576WGiDBdQ?t=12842

## What is this
MVP from creating a solidity contract, all the way to deploying it to a local chain using Web3.py and Ganache.

## Prerequisites
```bash
# https://web3py.readthedocs.io/en/stable/quickstart.html#installation
$ pip3 install web3

# https://pypi.org/project/python-dotenv/
$ pip3 install python-dotenv

# https://pypi.org/project/py-solc-x/
$ pip3 install py-solc-x

# https://yarnpkg.com/package/ganache
$ yarn add -g ganache
```



## Getting started
1. Start ganache locally
``` bash
$ ganache
ganache v7.0.3 (@ganache/cli: 0.1.4, @ganache/core: 0.1.4)
Starting RPC server

Available Accounts
==================
```

2. Pick a pair of public + private key. This'll be used for the subsequent steps

3. Set required environment variables in [.env](./.env)
```
// .env
export PRIVATE_KEY=<insert-account-private-key-here>
```

4. Update values at [./deploy.py](./deploy.py)
```python
// deploy.py
w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:7545")) # <- update port, if changed
chain_id = 1337
my_address = "<insert-account-public-key-here>" # <- update public key
private_key = os.getenv("PRIVATE_KEY")
```

5. Run deploy.py
```bash
$ python3 deploy.py
```

6. View transactions created in terminal