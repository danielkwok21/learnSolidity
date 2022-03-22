from brownie import MVP, accounts

def test_deploy():
    account = accounts[0]
    mvp_contract = MVP.deploy({"from":account})
    starting_value = mvp_contract.getGreeting()
    expected = ""

    assert starting_value == expected


def test_set_greeting():
    account = accounts[0]
    mvp_contract = MVP.deploy({"from":account})
    mvp_contract.setGreeting("Hello world", {"from":account})
    updated_value = mvp_contract.getGreeting()
    expected = "Hello world"

    assert updated_value == expected