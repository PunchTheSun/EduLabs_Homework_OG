# C7 - inheritance, apartments for sale and rent

class Apartment:
    def __init__(self, address: str, rooms_num: float, size_in_sq_meters: int, floor: int, monthly_municipal_tax: float,
                 deal_state: str = "open", parking_type: str = "No Parking", has_balcony: bool = False,
                 is_penthouse: bool = False, is_villa: bool = False):
        self._is_villa = is_villa
        self._is_penthouse = is_penthouse
        self._has_balcony = has_balcony
        self._parking_type = parking_type
        self._deal_state = deal_state
        self._monthly_municipal_tax = monthly_municipal_tax
        self._floor = floor
        self._size_in_sq_meters = size_in_sq_meters
        self._rooms_num = rooms_num
        self._address = address

    def get_annual_municipal_tax(self) -> float:
        return self._monthly_municipal_tax

    def close_deal(self) -> bool:
        self._deal_state = "closed"
        return True
