# Menus - Exceptions definitions

class InvalidUserInput(Exception):
    def __init__(self, user_input: str):
        super().__init__()
        self._user_input = user_input

    def __str__(self):
        return f"Invalid user input: {self._user_input}"


class NotNumber(Exception):
    def __init__(self, user_input: str):
        super().__init__()
        self._user_input = user_input

    def __str__(self):
        return f"Invalid user input: {self._user_input}'\nNot a valid number"


class NotStopName(Exception):
    def __init__(self, stop_name: str):
        super().__init__()
        self._stop_name = stop_name

    def __str__(self):
        return f"Invalid stop name: {self._stop_name}'\nNot a valid text"


class InvalidDelayedRideID(Exception):
    def __init__(self, delayed_ride_id: str):
        super().__init__()
        self._delayed_ride_id = delayed_ride_id

    def __str__(self):
        return f"Invalid delayed ride ID input: {self._delayed_ride_id}\nNot a number from the scheduled rides ID list"


class ListOfStopsAborted(Exception):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return f"The creation of the list of stops has been aborted"


class EmptyListOfStops(Exception):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return f"Invalid input - Empty list of stops detected"


class NotDriverName(Exception):
    def __init__(self, driver_name: str):
        super().__init__()
        self._driver_name = driver_name

    def __str__(self):
        return f"Invalid driver name: {self._driver_name}'\nNot a valid text"


class WrongTimeFormat(Exception):
    def __init__(self, time_type: str):
        super().__init__()
        self._time_type = time_type

    def __str__(self):
        return f"Invalid {self._time_type} time format given\nExample for a valid time format: 09:05"
