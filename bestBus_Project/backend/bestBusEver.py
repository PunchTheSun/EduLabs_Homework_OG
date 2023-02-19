# Best Bus Ever - Classes
import datetime
from backend.bestBusEver_Exceptions import *


class ScheduledRide:
    def __init__(self, ride_id: int, origin_time: datetime.time, destination_time: datetime.time, driver_name: str):
        self._driver_name = driver_name
        self._destination_time = destination_time
        self._origin_time = origin_time
        self._ride_id = ride_id
        self._delays = 0

    def get_driver_name(self) -> str:
        return self._driver_name

    def get_destination_time(self) -> datetime.time:
        return self._destination_time

    def get_origin_time(self) -> datetime.time:
        return self._origin_time

    def get_ride_id(self) -> int:
        return self._ride_id

    def get_delays(self) -> int:
        return self._delays

    def add_delay(self):
        self._delays += 1

    def __str__(self):
        return f"\nRide ID: {self._ride_id}\nOrigin Time: {self._origin_time}" \
               f"\nDestination Time: {self._destination_time}\nDelay Count: {self._delays}\n" \
               f"------------------------------------------"

    def __repr__(self):
        return f"\nRide ID: {self._ride_id}\nOrigin Time: {self._origin_time}" \
               f"\nDestination Time: {self._destination_time}\nDelay Count: {self._delays}\n" \
               f"------------------------------------------"

class BusRoute:
    def __init__(self, line_number: int, list_of_stops: list[str]):
        self._line_number = line_number
        self._list_of_stops = list_of_stops
        self._origin = list_of_stops[0]
        self._destination = list_of_stops[-1]
        self._scheduled_rides = []

    def get_line_number(self) -> int:
        return self._line_number

    def get_list_of_stops(self) -> list[str]:
        return self._list_of_stops

    def set_list_of_stops(self, new_list_of_stops: list[str]):
        if not isinstance(new_list_of_stops, list):
            raise TypeError
        for stop in new_list_of_stops:
            if not isinstance(stop, str):
                raise TypeError
        self._list_of_stops = new_list_of_stops
        self._origin = self._list_of_stops[0]
        self._destination = self._list_of_stops[-1]

    def get_origin_stop(self) -> str:
        return self._list_of_stops[0]

    def set_origin_stop(self, new_origin_stop: str):
        if not isinstance(new_origin_stop, str):
            raise TypeError
        self._list_of_stops[0] = new_origin_stop
        self._origin = self._list_of_stops[0]

    def get_destination_stop(self) -> str:
        return self._list_of_stops[-1]

    def set_destination_stop(self, new_destination_stop: str):
        if not isinstance(new_destination_stop, str):
            raise TypeError
        self._list_of_stops[-1] = new_destination_stop
        self._origin = self._list_of_stops[-1]

    def get_scheduled_rides(self) -> list[ScheduledRide]:
        return self._scheduled_rides[:]

    def add_scheduled_ride(self, new_ride: ScheduledRide):
        if not isinstance(new_ride, ScheduledRide):
            raise TypeError
        self._scheduled_rides.append(new_ride)
        self._scheduled_rides.sort(key=lambda ride_time: new_ride.get_origin_time())

    def __str__(self):
        return f"Line Number: {self._line_number}\nOrigin: {self._origin}\nDestination: {self._destination}\n\n"\
               f"Entire Route: {self._list_of_stops}\n\nScheduled Rides: {self._scheduled_rides}" \
               f"\n*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*"

    def __repr__(self):
        return f"Line Number: {self._line_number}\nOrigin: {self._origin}\nDestination: {self._destination}\n\n"\
               f"Entire Route: {self._list_of_stops}\n\nScheduled Rides: \n{self._scheduled_rides}" \
               f"\n*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*"


class BestBusCompany:
    def __init__(self):
        self._list_of_routes = []

    def check_line_exist(self, line_number: int) -> bool:
        for route in self._list_of_routes:
            if line_number == route.get_line_number():
                return True
        return False

    def get_line_index(self, line_number: int) -> int:
        for i, route in enumerate(self._list_of_routes):
            if line_number == route.get_line_number():
                return i
        raise LineNotExists(line_number)

    def get_scheduled_ride_index(self, line_index: int, scheduled_ride_id: int) -> int:
        for i, scheduled_ride in enumerate(self._list_of_routes[line_index].get_scheduled_rides()):
            if scheduled_ride_id == scheduled_ride.get_ride_id():
                return i
        raise RideNotExists(scheduled_ride_id)

    def add_route(self, line_number: int, list_of_stops: list[str]):
        if self.check_line_exist(line_number):
            raise LineAlreadyExists(line_number)
        new_route = BusRoute(line_number, list_of_stops)
        self._list_of_routes.append(new_route)
        self._list_of_routes.sort(key=lambda route_number: route_number.get_line_number())
        print(f"Route number {line_number} was added successfully")

    def delete_route(self, line_number: int):
        if not self.check_line_exist(line_number):
            raise LineNotExists(line_number)
        del_index = self.get_line_index(line_number)
        self._list_of_routes.pop(del_index)
        print(f"Route number: {line_number} was deleted successfully")

    def update_origin_stop(self, line_number: int, new_origin_stop: str):
        if not self.check_line_exist(line_number):
            raise LineNotExists(line_number)
        update_index = self.get_line_index(line_number)
        self._list_of_routes[update_index].set_origin_stop(new_origin_stop)
        print(f"Route number {line_number} origin stop was updated successfully")

    def update_destination_stop(self, line_number: int, new_destination_stop: str):
        if not self.check_line_exist(line_number):
            raise LineNotExists(line_number)
        update_index = self.get_line_index(line_number)
        self._list_of_routes[update_index].set_origin_stop(new_destination_stop)
        print(f"Route number {line_number} destination stop was updated successfully")

    def update_list_of_stops(self, line_number: int, new_list_of_stops: list[str]):
        if not self.check_line_exist(line_number):
            raise LineNotExists(line_number)
        update_index = self.get_line_index(line_number)
        self._list_of_routes[update_index].set_list_of_stops(new_list_of_stops)
        print(f"Route number {line_number} stops were updated successfully")

    def get_line_existing_rides_list(self, line_number: int) -> list[ScheduledRide]:
        if not self.check_line_exist(line_number):
            raise LineNotExists(line_number)
        display_index = self.get_line_index(line_number)
        return self._list_of_routes[display_index].get_scheduled_rides()

    def get_all_routes(self) -> list[BusRoute]:
        return self._list_of_routes

    def add_scheduled_ride_to_line(self, line_number: int, origin_time: datetime.time, destination_time: datetime.time, driver_name: str):
        if not self.check_line_exist(line_number):
            raise LineNotExists(line_number)
        new_ride_index = self.get_line_index(line_number)
        new_ride = ScheduledRide(len(self._list_of_routes[new_ride_index].get_scheduled_rides())+1, origin_time, destination_time, driver_name)
        self._list_of_routes[new_ride_index].add_scheduled_ride(new_ride)

    def search_route_by_line_number(self, line_number: int) -> list[BusRoute]:
        ret_list = []
        for route in self._list_of_routes:
            if line_number == route.get_line_number():
                ret_list.append(route)
        if not ret_list:
            raise LineNotExists(line_number)
        return ret_list

    def search_route_by_origin_stop(self, origin_stop: str) -> list[BusRoute]:
        ret_list = []
        for route in self._list_of_routes:
            if origin_stop.lower() == route.get_origin_stop().lower():
                ret_list.append(route)
        if not ret_list:
            raise OriginNotExists(origin_stop)
        return ret_list

    def search_route_by_destination_stop(self, destination_stop: str) -> list[BusRoute]:
        ret_list = []
        for route in self._list_of_routes:
            if destination_stop.lower() == route.get_destination_stop().lower():
                ret_list.append(route)
        if not ret_list:
            raise DestinationNotExists(destination_stop)
        return ret_list

    def search_route_by_any_stop(self, any_stop: str) -> list[BusRoute]:
        ret_list = []
        for route in self._list_of_routes:
            for stop in route.get_list_of_stops():
                if any_stop == stop:
                    ret_list.append(route)
        if not ret_list:
            raise StopNotExists(any_stop)
        return ret_list

    def report_delay(self, delayed_route_line_number: int, delayed_route_scheduled_ride_id: int):
        delayed_route_index = self.get_line_index(delayed_route_line_number)
        delayed_scheduled_ride_index = self.get_scheduled_ride_index(delayed_route_index, delayed_route_scheduled_ride_id)
        scheduled_rides = self._list_of_routes[delayed_route_index].get_scheduled_rides()
        scheduled_rides[delayed_scheduled_ride_index].add_delay()
        print(f"Line: {delayed_route_line_number}, Ride ID: {delayed_route_scheduled_ride_id} - Delay added."
              f"\nThank you for reporting the delay, We apologize for the inconvenience.")
