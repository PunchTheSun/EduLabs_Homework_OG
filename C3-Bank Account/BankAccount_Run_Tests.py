# BankAccount - Run Tests
from BankAccount_Tests import *

if __name__ == "__main__":
    print("Running tests\n.\n.\n.")
    test_deposit1()
    test_deposit2()
    test_deposit3()
    test_deposit4()
    test_withdraw1()
    test_withdraw2()
    test_withdraw3()
    test_get_transactions_per_date() # Please change the string text for the date to be the correct current date today.
    print(".\n.\n.\nTests finished, No assertions detected - Good job!")