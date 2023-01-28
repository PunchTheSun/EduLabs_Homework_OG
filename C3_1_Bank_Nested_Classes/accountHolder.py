# C3_1 AccountHolder Class

class AccountHolder:

    def __init__(self, holder_id: str, name: str, bday: str, address: str, credit_score: float):
        self._credit_score = credit_score
        self._address = address
        self._bday = bday
        self._name = name
        self._holder_id = holder_id

    def get_name(self) -> str:
        return self._name

    def update_name(self, new_name: str) -> bool:
        if not isinstance(new_name, str):
            return False
        self._name = new_name
        return True

    def update_bday(self, new_bday: str) -> bool:
        if not isinstance(new_bday, str):
            return False
        self._bday = new_bday
        return True

    def update_address(self, new_address: str) -> bool:
        if not isinstance(new_address, str):
            return False
        self._address = new_address
        return True

    def update_credit_score(self, new_credit_score: float) -> bool:
        if not isinstance(new_credit_score, float):
            return False
        self._credit_score = new_credit_score
        return True
