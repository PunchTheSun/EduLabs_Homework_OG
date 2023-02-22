from concurrent.futures import ThreadPoolExecutor
from bank_Account.bank_Nested_Classes.bankAccount_Class import BankAccount

if __name__ == "__main__":
    # this code should run without problems
    if __name__ == '__main__':
        account = BankAccount(123456, "Israel Israeli", "Israel_street", "052-9999999")

        def multiple_transactions_deposit(user_account):
            for i in range(100, 2000000, 10):
                user_account.deposit(float(i))


        def multiple_transactions_withdraw(user_account):
            for i in range(100, 2000000, 10):
                user_account.withdraw(float(i))


        with ThreadPoolExecutor(4) as executor:
            executor.submit(multiple_transactions_deposit, account)
            executor.submit(multiple_transactions_withdraw, account)

        assert account._nis_balance == 0, \
            f"Expected balance: 0, received: {account._nis_balance}"
        assert len(account._transaction_list) == 399980, \
            f"Expected transactions: 399980, received: {len(account._transaction_list)}"
