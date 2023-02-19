# Client Main Menu Functions
from frontend.menus_Exceptions import *


def client_main_menu_display_msg() -> int:
    choice = input("\n1) Search route\n2) Report a delay\n3) Display all routes\n4) Logout"
                   "\n\nPlease enter an option from the menu (1/2/3/4): ")
    print("")
    if choice.isnumeric() and choice in {'1', '2', '3', '4'}:
        return int(choice)
    else:
        raise InvalidUserInput(choice)


def client_search_by() -> int:
    search_type = input("Search by:\n1) Line number\n2) Origin\n3) Destination\n4) Stop along the way\n\nPlease enter an option from the menu (1/2/3/4): ")
    print("")
    if search_type.isnumeric() and search_type in {'1', '2', '3', '4'}:
        return int(search_type)
    else:
        raise InvalidUserInput(search_type)


def verify_delayed_ride_id(scheduled_rides_ids: list[int]) -> int:
    delayed_ride_id = input("Please enter the delayed ride's ID number: ")
    print("")
    if delayed_ride_id.isnumeric():
        if int(delayed_ride_id) in scheduled_rides_ids:
            return int(delayed_ride_id)
    raise InvalidDelayedRideID(delayed_ride_id)
