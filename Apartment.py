# Apartment Class
import Bathroom


class Apartment:

    def __init__(self, address: str, apt_floor: int, building_floors: int, rooms: list[float], bathroom: Bathroom,
                 kitchen_size: float, balconies: list[float] = [0.0]):
        self.__address = address
        self.__apt_floor = apt_floor
        self.__building_floors = building_floors
        self.__rooms = rooms
        self.__bathroom = bathroom
        self.__kitchen_size = kitchen_size
        self.__balconies = balconies

    def get_rooms_number(self) -> int:
        return len(self.__rooms)

    def is_last_floor(self) -> bool:
        if self.__apt_floor == self.__building_floors:
            return True
        return False

    def get_total_apartment_size(self) -> float:
        total_size = 0.0
        for room in self.__rooms:
            total_size += room
        for balcony in self.__balconies:
            total_size += balcony
        return total_size

    def get_total_living_space_size(self) -> float:
        total_living_size = 0.0
        for room in self.__rooms:
            total_living_size += room
        return total_living_size

    def get_total_area_of_balconies(self) -> float:
        total_balconies_size = 0.0
        for balcony in self.__balconies:
            total_balconies_size += balcony
        return total_balconies_size

    def get_annual_arnona(self, sqft_rate: float) -> float:
        annual_arnona = (self.get_total_living_space_size() * sqft_rate) +\
                        (self.get_total_area_of_balconies() * sqft_rate * 0.75)
        return annual_arnona
