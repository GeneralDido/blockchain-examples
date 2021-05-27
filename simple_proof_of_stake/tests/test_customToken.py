# pass -s to the flag to see print statements
import brownie
from brownie import accounts


def test_account_balance():
    balance = accounts[0].balance()
    accounts[0].transfer(accounts[1], "1 ether", gas_price=0)
    assert balance - "1 ether" == accounts[0].balance()


def test_staking(CustomToken):
    token = accounts[0].deploy(CustomToken)
    token.initialize(accounts[0], 1000, 1000000, 0, 1000, 2, CustomToken[0])

    token.transfer(accounts[1], 300)
    token.initializeBalance(accounts[1])
    token._stake(accounts[1], 1)

    assert token.stakeOf(accounts[1]) == 1
    assert token.getBalance(accounts[1]) == 299

    token._unstake(accounts[1])
    assert token.getBalance(accounts[1]) == 300

    token.transfer(accounts[2], 200)
    token.initializeBalance(accounts[2])

    token._stake(accounts[2], 10)
    assert token.getBalance(accounts[2]) == 190
    token._stake(accounts[1], 10)
    assert token.getBalance(accounts[1]) == 290

    token._unstake(accounts[2])
    assert token.getBalance(accounts[2]) == 200
    token._unstake(accounts[1])
    assert token.getBalance(accounts[1]) == 300
