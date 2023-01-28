# C5 - TableReservationSystem Class
import datetime

from table import Table


class TableReservationSystem:

    def __init__(self, restaurant_name: str, max_time_limit: datetime.timedelta, tables: list[Table]):
        self._max_time_limit = max_time_limit
        self._restaurant_name = restaurant_name
        self._tables = tables

    def get_available_tables(self, num_of_guests: int) -> list[Table]:
        ret_list = []
        for table_val in self._tables:
            if table_val.num_of_seats < num_of_guests and not table_val.is_occupied:
                ret_list.append(table_val)

        if not ret_list or len(ret_list) == 1:
            return ret_list

        found_something = True
        while found_something:
            found_something = False
            for i, in range(len(ret_list), 0, -1):
                if ret_list[i].num_of_seats < ret_list[i-1].num_of_seats:
                    temp_table = ret_list[i-1]
                    ret_list[i-1] = ret_list[i]
                    ret_list[i] = temp_table
                    found_something = True
        return ret_list

    def get_soonest_available_tables(self, num_of_guests: int) -> list[Table]:
        ret_list = self.get_available_tables(num_of_guests)

        if not isinstance(ret_list, list) or not isinstance(ret_list[0], Table) or not ret_list:
            return ret_list

        found_something = True
        while found_something:
            found_something = False
            for i, in range(len(ret_list), 0, -1):
                if ret_list[i].time_left() < ret_list[i-1].time_left():
                    temp_table = ret_list[i - 1]
                    ret_list[i - 1] = ret_list[i]
                    ret_list[i] = temp_table
                    found_something = True
        return ret_list

    def reserve_a_table(self, table_id: int, num_of_guests: int) -> bool:
        reservation_succeeded = bool()
        for table in self._tables:
            if table.table_id == table_id:
                reservation_succeeded = table.reserve_a_table(num_of_guests)
            return reservation_succeeded

    def release_a_table(self, table_id: int) -> bool:
        release_succeeded = bool()
        for table in self._tables:
            if table.table_id == table_id:
                release_succeeded = table.release_a_table()
            return release_succeeded

    def get_tables_with_less_than_x_minutes_left(self, num_of_seats: int, num_of_minutes: int):
        ret_list = list()
        for table in self._tables:
            if table.time_left().total_seconds() / 60 < num_of_minutes and table.num_of_seats >= num_of_seats \
                    or not table.is_occupied and table.num_of_seats >= num_of_seats:
                ret_list.append(table)
        return ret_list

    def get_tables_time_limit(self) -> datetime.timedelta:
        return self._max_time_limit

    def update_table_time_limit(self, new_time_limit: datetime.timedelta) -> bool:
        if not isinstance(new_time_limit, datetime.timedelta):
            return False
        self._max_time_limit = new_time_limit
        return True
