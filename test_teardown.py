import pytest
from bank import BankAccount


@pytest.fixture
def account():
    print("[setup]")
    acct = BankAccount(100)
    yield acct
    print("[teardown]")


def test_starting_balance(account):
    assert account.balance == 100


def test_deposit_with_teardown(account):
    account.deposit(50)
    assert account.balance == 150