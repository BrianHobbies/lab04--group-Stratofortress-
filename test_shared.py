def test_funded_account_balance(funded_account):
    assert funded_account.balance == 1000


def test_withdraw_from_funded_account(funded_account):
    funded_account.withdraw(300)
    assert funded_account.balance == 700
    