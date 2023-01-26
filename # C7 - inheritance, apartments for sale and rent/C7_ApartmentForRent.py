# C7 Apartment For Rent class

from C7_Apartment_Class import Apartment


class ApartmentForRent(Apartment):
    def __init__(self, address: str, rooms_num: float, size_in_sq_meters: int, floor: int,
                 monthly_municipal_tax: float, rent_price_per_month: float, pets_allowed: bool = False):
        super().__init__(address, rooms_num, size_in_sq_meters, floor, monthly_municipal_tax)
        self._pets_allowed = pets_allowed
        self._rent_price_per_month = rent_price_per_month

    def get_agency_fee(self) -> float:
        return 0.02*self._rent_price_per_month
