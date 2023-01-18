# BankAccount Class
import datetime


class BankAccount:

    def __init__(self, account_num: int, passport_num: int, address: str, phone: str, is_usd_allowed: bool = False, maximum_credit_lim: float = -10000.0):
        self.__phone = phone
        self.__address = address
        self.__account_num = account_num
        self.__passport_num = passport_num
        self.__nis_balance = 0.0
        self.__usd_balance = 0.0
        self.__is_usd_allowed = is_usd_allowed
        self.__maximum_credit_lim = maximum_credit_lim
        self.__transaction_data = {}

    @staticmethod
    def get_now_time_formatted() -> str:
        now_time_formatted = ["", "", ""]
        now_time = str(datetime.datetime.now())
        now_time, *throwaway = now_time.split(" ")
        now_time_formatted[2], now_time_formatted[1], now_time_formatted[0] = now_time.split("-")
        return str(now_time_formatted[0]+"-"+now_time_formatted[1]+"-"+now_time_formatted[2])

    def get_phone(self) -> str:
        return self.__phone

    def set_phone(self, new_phone: str) -> bool:
        self.__phone = new_phone
        return True

    def get_address(self) -> str:
        return self.__address

    def set_address(self, new_address: str) -> bool:
        self.__address = new_address
        return True

    def get_account_num(self) -> int:
        return self.__account_num

    def set_account_num(self, new_account_num: int) -> bool:
        self.__account_num = new_account_num
        return True

    def get_passport_num(self) -> int:
        return self.__passport_num

    def set_passport_num(self, new_passport_num: int) -> bool:
        self.__passport_num = new_passport_num
        return True

    def get_nis_balance(self) -> float:
        return self.__nis_balance

    def get_usd_balance(self) -> float:
        return self.__usd_balance

    def get_is_usd_allowed(self) -> bool:
        return self.__is_usd_allowed

    def set_is_usd_allowed(self, new_is_usd_allowed: bool) -> bool:
        self.__is_usd_allowed = new_is_usd_allowed
        return True

    def get_maximum_credit_lim(self) -> float:
        return self.__maximum_credit_lim

    def set_maximum_credit_lim(self, new_maximum_credit_lim: float) -> bool:
        self.__maximum_credit_lim = new_maximum_credit_lim
        return True

    def get_transaction_data(self) -> dict[dict]:
        return self.__transaction_data

    def add_new_transaction(self, date: str, transaction_type: str, currency: str, amount: float) -> bool:
        new_transaction_dict = {"date": date, "type": transaction_type, "currency": currency, "amount": amount}
        if self.__transaction_data:
            self.__transaction_data[date] = (self.__transaction_data[date], new_transaction_dict)
        else:
            self.__transaction_data[date] = new_transaction_dict
        return True

    def deposit(self, amount: float, currency: str = "nis") -> bool:
        if not isinstance(amount, float) or amount < 0:
            print("Invalid deposit amount input\nMust be a number and larger than 0")
            return False
        match currency.lower():
            case "nis":
                self.__nis_balance += amount
            case "usd":
                if self.__is_usd_allowed:
                    self.__usd_balance += amount
                else:
                    print("Account doesn't have USD balance")
                    return False
            case _:
                print("Invalid currency input\nPlease select between 'nis' or 'usd'")
                return False
        self.add_new_transaction(self.get_now_time_formatted(), "deposit", currency, amount)
        return True

    def withdraw(self, amount: float, currency: str = "nis") -> bool:
        if not isinstance(amount, float) or amount < 0:
            print("Invalid withdraw amount input\nMust be a number and larger than 0")
            return False
        match currency.lower():
            case "nis":
                new_nis_balance = self.__nis_balance - amount
                if new_nis_balance >= self.__maximum_credit_lim:
                    self.__nis_balance = new_nis_balance
                else:
                    print(f"Current NIS Balance: {self.__nis_balance}\nWith a credit limit of {self.__maximum_credit_lim}\nNot enough balance to withdraw {amount} NIS")
                    return False
            case "usd":
                if self.__is_usd_allowed:
                    new_usd_balance = self.__usd_balance - amount
                    if new_usd_balance >= 0:
                        self.__usd_balance += new_usd_balance
                    else:
                        print(f"Current USD Balance: {self.__usd_balance}\nNot enough balance to withdraw {amount} USD")
                        return False
                else:
                    print("Account doesn't have USD balance")
                    return False
            case _:
                print("Invalid currency input\nPlease select between 'nis' or 'usd'")
                return False
        self.add_new_transaction(self.get_now_time_formatted(), "withdraw", currency, amount)
        return True

    def convert(self, amount: float, to_currency: str) -> bool:
        if not isinstance(amount, float) or amount < 0:
            print("Invalid conversion amount input\nMust be a number and larger than 0")
            return False
        if not self.__is_usd_allowed:
            print("This account doesn't have a USD balance")
            return False
        match to_currency.lower():
            case "nis":
                new_usd_balance = self.__usd_balance - amount
                if new_usd_balance < 0:
                    print("Can't convert, Insufficient USD balance")
                    return False
                else:
                    self.__usd_balance = new_usd_balance
                    self.__nis_balance += amount * 3.42
            case "usd":
                new_nis_balance = self.__nis_balance - amount
                if new_nis_balance < self.__maximum_credit_lim:
                    print("Can't convert, Insufficient NIS balance\nExceeding maximum credit limit")
                    return False
                else:
                    self.__nis_balance = new_nis_balance
                    self.__usd_balance += amount * 0.29
            case _:
                print("Invalid currency input\nPlease select between 'nis' or 'usd'")
                return False
        self.add_new_transaction(self.get_now_time_formatted(), "conversion", to_currency, amount)
        return True

    def get_current_balance(self, currency: str = "   ") -> None | float:
        match currency.lower():
            case "nis":
                return self.__nis_balance
            case "usd":
                if self.__is_usd_allowed:
                    return self.__usd_balance
                else:
                    print("This account doesn't have a USD balance")
            case "   ":
                if self.__is_usd_allowed:
                    print(f"NIS Balance: {self.__nis_balance}\nUSD Balance: {self.__usd_balance}")
                else:
                    print(f"NIS Balance: {self.__nis_balance}")
        return

    def get_transactions_per_date(self, transaction_date: str) -> list[dict]:
        ret_list = []
        for date in self.__transaction_data.keys():
            if date == transaction_date:
                ret_list.append(self.__transaction_data[transaction_date])
        return ret_list

    def get_monthly_cash_flow(self, selected_month: str, selected_year: str) -> list[int]:
        deposits = 0
        withdrawals = 0
        for date in self.__transaction_data.keys():
            date_tuple = date.split("-")
            if date_tuple[1] == selected_month and date_tuple[2] == selected_year:
                match self.__transaction_data[date]["type"]:
                    case "withdraw":
                        withdrawals += self.__transaction_data[date]["amount"]
                    case "deposit":
                        deposits += self.__transaction_data[date]["amount"]
        ret_list = [deposits, withdrawals]
        return ret_list

    def __iadd__(self, other):
        if type(other) in (int, float):
            self.deposit(other)
        return self

    def __eq__(self, other):
        if type(other) == BankAccount:
            if self.__account_num == BankAccount(other).__account_num:
                return True
        return False

    def __ne__(self, other):
        if type(other) == BankAccount:
            if self.__account_num != BankAccount(other).__account_num:
                return True
        return False

    def __int__(self):
        return self.__account_num

