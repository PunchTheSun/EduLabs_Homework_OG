# BankAccount Class Tests

from BankAccount_Class import BankAccount


def test_withdraw1():
    account = BankAccount(1, 101, "Banana street", "0528991659")
    ret_val = account.withdraw(30000.0)

    assert ret_val is False, "We shouldn't have enough balance to draw from"


def test_withdraw2():
    account = BankAccount(1, 101, "Banana street", "0528991659")
    account.deposit(30000.0)
    ret_val = account.withdraw(30000.0)

    assert ret_val is True, "We should have enough balance to draw from"


def test_withdraw3():
    account = BankAccount(1, 101, "Banana street", "0528991659")
    account.deposit(30000)
    ret_val = account.withdraw(-1.0)

    assert ret_val is False, "We can't withdraw a negative value"


def test_deposit1():
    account = BankAccount(1, 101, "Banana street", "0528991659")
    ret_val = account.deposit(-1.0)

    assert ret_val is False, "We can't deposit a negative value"


def test_deposit2():
    account = BankAccount(1, 101, "Banana street", "0528991659")
    ret_val = account.deposit(100.0, "usd")

    assert ret_val is False, "We can't deposit USD while self.__is_usd_allowed == False"


def test_deposit3():
    account = BankAccount(1, 101, "Banana street", "0528991659")
    account.set_is_usd_allowed(True)
    ret_val = account.deposit(100.0, "usd")

    assert ret_val is True, "We can deposit USD while self.__is_usd_allowed == True"


def test_deposit4():
    account = BankAccount(1, 101, "Banana street", "0528991659")
    ret_val = account.deposit("bonkers")

    assert ret_val is False, "amount must be a float and higher than 0"


def test_get_transactions_per_date():
    account = BankAccount(1, 101, "Banana street", "0528991659")
    account.deposit(300.0)
    account.deposit(700.0)
    ret_val = account.get_transactions_per_date("17-01-2023") # Please change the date to match today while testing
    expected = [({"date": "17-01-2023", "type": "deposit", "currency": "nis", "amount": 300.0}, {"date": "17-01-2023", "type": "deposit", "currency": "nis", "amount": 700.0})]

    assert ret_val == expected, f"Expected: {expected}\nReceived: {ret_val}"