# C3_1 BankBranch Class

class BankBranch:

    def __init__(self, branch_id: str, name: str, city: str, address: str):
        self._address = address
        self._city = city
        self._name = name
        self._branch_id = branch_id

    def get_city(self) -> str:
        return self._city

    def update_name(self, new_name: str) -> bool:
        if not isinstance(new_name, str):
            return False
        self._name = new_name
        return True

    def update_city(self, new_city: str) -> bool:
        if not isinstance(new_city, str):
            return False
        self._city = new_city
        return True

    def update_address(self, new_address: str) -> bool:
        if not isinstance(new_address, str):
            return False
        self._address = new_address
        return True
