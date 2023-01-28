# C3_1 Bank Class
from bankAccount_Class import BankAccount
from accountHolder import AccountHolder
from bankBranch import BankBranch


class Bank:

    def __init__(self, bank_name: str, bank_hq_address: str, branches: dict[str, BankBranch],
                 accounts: dict[str, BankAccount], customers: dict[str, AccountHolder],
                 link_customer_accounts: dict[str, str]):
        self._customers = customers
        self._accounts = accounts
        self._branches = branches
        self._bank_hq_address = bank_hq_address
        self._bank_name = bank_name
        self._link_customer_accounts = link_customer_accounts

    def link_accounts(self, customer_id_to_link: str,
                      account_id_to_link: str) -> bool:  # customer_id = Key || account_ids = Values
        if not isinstance(customer_id_to_link, str) or not isinstance(account_id_to_link, str):
            return False
        if customer_id_to_link in self._link_customer_accounts.keys():
            self._link_customer_accounts[customer_id_to_link] = \
                f"{self._link_customer_accounts[customer_id_to_link]},{account_id_to_link}"
        else:
            self._link_customer_accounts[customer_id_to_link] = account_id_to_link
        return True

    def add_branch(self, branch_id: str, branch_name: str, branch_city: str, branch_address: str) -> bool:
        if not branch_id.isnumeric() or not branch_name.isalpha() \
                or not branch_city.isalpha() or not branch_address.isalpha():
            return False
        new_branch = {branch_id: BankBranch(branch_id, branch_name, branch_city, branch_address)}
        self._branches.update(new_branch)
        return True

    def get_branch_by_id(self, branch_id: str) -> BankBranch:
        return self._branches.get(branch_id, "ID Doesn't exist in database")

    def get_branch_by_city(self, branch_city: str) -> list[BankBranch]:
        ret_list = []
        if not self._branches:
            return ret_list
        for branch_id in self._branches.keys():
            if self._branches[branch_id].get_city().lower() == branch_city.lower():
                ret_list.append(self._branches[branch_id])
        return ret_list

    def update_branch_details(self, branch_id: str, branch_name: str = None,
                              branch_city: str = None, branch_address: str = None) -> bool:
        if branch_id not in self._branches.keys():
            return False
        if branch_name is not None:
            self._branches[branch_id].update_name(branch_name)
        if branch_city is not None:
            self._branches[branch_id].update_city(branch_city)
        if branch_address is not None:
            self._branches[branch_id].update_address(branch_address)
        return True

    def delete_branch(self, branch_id) -> bool:
        if branch_id not in self._branches.keys():
            return False
        self._branches.pop(branch_id)
        return True

    def add_customer(self, customer_id: str, customer_name: str, customer_bday: str, customer_address: str) -> bool:
        if not customer_id.isnumeric() or not customer_name.isalpha() \
                or not customer_address.isalpha():
            return False
        new_customer = {customer_id: AccountHolder(customer_id, customer_name,
                                                   customer_bday, customer_address, credit_score=0.0)}
        self._customers.update(new_customer)
        return True

    def get_customer_by_id(self, customer_id: str) -> AccountHolder:
        return self._customers.get(customer_id, "ID Doesn't exist in database")

    def get_customer_by_name(self, customer_name: str) -> list[AccountHolder]:
        ret_list = []
        if not self._customers:
            return ret_list
        for customer_id in self._customers.keys():
            if self._customers[customer_id].get_name().lower() == customer_name.lower():
                ret_list.append(self._customers[customer_id])
        return ret_list

    def update_customer_details(self, customer_id: str, customer_name: str = None,
                                customer_bday: str = None, customer_address: str = None,
                                customer_credit_score: float = None) -> bool:
        if customer_id not in self._customers.keys():
            return False
        if customer_name is not None:
            self._customers[customer_id].update_name(customer_name)
        if customer_bday is not None:
            self._customers[customer_id].update_bday(customer_bday)
        if customer_address is not None:
            self._customers[customer_id].update_address(customer_address)
        if customer_credit_score is not None:
            self._customers[customer_id].update_credit_score(customer_credit_score)
        return True

    def delete_customer(self, customer_id: str) -> bool:
        if customer_id not in self._customers.keys():
            return False
        self._customers.pop(customer_id)
        return True

    def get_customer_accounts(self, customer_id: str) -> list[BankAccount]:
        ret_list = []
        if customer_id not in self._customers.keys() or customer_id not in self._link_customer_accounts.keys():
            return ret_list
        account_ids = self._link_customer_accounts[customer_id].split(",")
        for account_id in account_ids:
            if account_id in self._accounts.keys():
                ret_list.append(self._accounts[account_id])
        return ret_list

    def add_account(self, account_num: int, passport_num: int, address: str, phone: str, is_usd_allowed: bool = False,
                    maximum_credit_lim: float = -10000.0) -> bool:
        if account_num in self._accounts.keys() or not isinstance(passport_num, int) or not address.isalpha() \
                                                or not isinstance(phone, str) or not isinstance(is_usd_allowed, bool) \
                                                or not isinstance(maximum_credit_lim, float):
            return False
        self._accounts[str(account_num)] = BankAccount(account_num, passport_num, address, phone,
                                                       is_usd_allowed, maximum_credit_lim)
        return True

    def deposit(self, account_num: str, amount: float, currency: str = "nis") -> bool:
        result = self._accounts[account_num].deposit(amount, currency)
        return result

    def withdraw(self, account_num: str, amount: float, currency: str = "nis") -> bool:
        result = self._accounts[account_num].withdraw(amount, currency)
        return result

    def transfer(self, account_num_from: str, account_num_to: str, amount: float, currency: str = "nis") -> bool:
        result_withdraw = self._accounts[account_num_from].withdraw(amount, currency)
        if not result_withdraw:
            return False
        result_deposit = self._accounts[account_num_to].deposit(amount, currency)
        if not result_deposit:
            self._accounts[account_num_from].deposit(amount, currency)
            return False
        return True

    def get_account_by_id(self, account_number: str) -> BankAccount:
        return self._accounts.get(account_number, "Account-Number Doesn't exist in database")

    def get_account_by_holder_id(self, holder_id: str) -> list[BankAccount]:
        return self.get_customer_accounts(holder_id)
