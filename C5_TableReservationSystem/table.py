# C5 - Table Class
import datetime


class Table:
    def __init__(self, table_id: int, num_of_seats: int, table_location: str, time_limit: datetime.timedelta,
                 num_of_floor: int = 1, is_occupied: bool = False,
                 reservation_start_time: datetime.time = datetime.time()):
        self.reservation_start_time = reservation_start_time
        self.reservation_end_time = datetime.time()
        self.is_occupied = is_occupied
        self.num_of_floor = num_of_floor
        self.table_location = table_location
        self.num_of_seats = num_of_seats
        self.table_id = table_id
        self._time_limit = time_limit

    def is_available(self):
        return self.is_occupied

    def reserve_a_table(self, num_of_guests: int) -> bool:
        if self.is_occupied or self.num_of_seats < num_of_guests:
            return False
        self.reservation_start_time = datetime.datetime.now().time()
        self.reservation_end_time = (datetime.datetime.now() + self._time_limit).time()
        self.is_occupied = True
        return True

    def release_a_table(self) -> bool:
        if not self.is_occupied:
            return False
        self.reservation_start_time = None
        self.reservation_end_time = None
        self.is_occupied = False
        return True

    def time_left(self) -> datetime.timedelta | bool:
        if not self.is_occupied:
            return False
        return datetime.datetime.combine(datetime.datetime.today(), self.reservation_end_time) - datetime.datetime.now()

    def get_available_hour(self) -> datetime.time | bool:
        if not self.is_occupied:
            return False
        return self.reservation_end_time

    def __str__(self):
        return f"Table ID: {self.table_id}\nSeats: {self.num_of_seats}" \
               f"\nFloor|Location: {self.num_of_floor}|{self.table_location}"
