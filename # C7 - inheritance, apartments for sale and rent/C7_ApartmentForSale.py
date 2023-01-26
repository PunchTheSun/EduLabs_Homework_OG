# C7 Apartment For Sale class

from C7_Apartment_Class import Apartment


class ApartmentForSale(Apartment):

    def __init__(self, address: str, rooms_num: float, size_in_sq_meters: int, floor: int,
                 monthly_municipal_tax: float, sale_price: float):
        super().__init__(address, rooms_num, size_in_sq_meters, floor, monthly_municipal_tax)
        self._sale_price = sale_price

    def get_agency_fee(self) -> float:
        return 0.02*self._sale_price
