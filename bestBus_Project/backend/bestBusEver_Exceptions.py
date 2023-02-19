# Best Bus Ever - Exceptions definitions

class LineAlreadyExists(Exception):
    def __init__(self, line_number: int):
        super().__init__()
        self._line_number = line_number

    def __str__(self):
        return f"Line number: {self._line_number} already exists"


class LineNotExists(Exception):
    def __init__(self, line_number: int):
        super().__init__()
        self._line_number = line_number

    def __str__(self):
        return f"Line number: {self._line_number} doesn't exist"


class RideNotExists(Exception):
    def __init__(self, ride_id: int):
        super().__init__()
        self._ride_id = ride_id

    def __str__(self):
        return f"Ride ID number: {self._ride_id} doesn't exist"


class OriginNotExists(Exception):
    def __init__(self, origin_stop: str):
        super().__init__()
        self._origin_stop = origin_stop

    def __str__(self):
        return f"Origin Stop: {self._origin_stop} doesn't exist"


class DestinationNotExists(Exception):
    def __init__(self, destination_stop: str):
        super().__init__()
        self._destination_stop = destination_stop

    def __str__(self):
        return f"Destination Stop: {self._destination_stop} doesn't exist"


class StopNotExists(Exception):
    def __init__(self, any_stop: str):
        super().__init__()
        self._any_stop = any_stop

    def __str__(self):
        return f"The Stop: {self._any_stop} doesn't exist"
