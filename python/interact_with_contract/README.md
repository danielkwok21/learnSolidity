# Interact with contract
Reference video timestamp: https://youtu.be/M576WGiDBdQ?t=14944

## What is this
How to interact with a deployed contract using python.
<br />Introduction to `call()`.
<br />This code is built on top of [../mvp](../mvp).


## Prerequisites
```bash
# https://web3py.readthedocs.io/en/stable/quickstart.html#installation
$ pip3 install web3

# https://pypi.org/project/python-dotenv/
$ pip3 install python-dotenv

# https://pypi.org/project/py-solc-x/
$ pip3 install py-solc-x

```

## Getting started
1. Start ganache locally

2. Set required environment variables in [.env](./.env)
```
// .env
export PRIVATE_KEY=<insert-account-private-key-here>
```

3. Update values at [./deploy.py](./deploy.py)
```python
// deploy.py
w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:7545"))
chain_id = 1337
my_address = "<insert-account-public-key-here>" # <- update public key
private_key = os.getenv("PRIVATE_KEY")
```

3. Run deploy.py
```bash
$ python3 deploy.py
```

4. View terminal
5. View "CONTRACT CREATION" and "CONTRACT CALL" via Ganache > Transactions