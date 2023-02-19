# Manager Main Menu Functions
import datetime

from frontend.menus_Exceptions import *


def manager_main_menu_display_msg() -> int:
    choice = input("\n1) Add route\n2) Delete route\n3) Update Route\n4) Add scheduled ride to route\n5) Logout"
                   "\n\nPlease enter an option from the menu (1/2/3/4/5): ")
    print("")
    if choice.isnumeric() and choice in {'1', '2', '3', '4', '5'}:
        return int(choice)
    else:
        raise InvalidUserInput(choice)


def create_list_of_stops(line_number: int) -> list[str]:
    new_list_of_stops = []
    stop_number = 1
    new_stop = ""
    print(f"Please enter the names of the stops for route number {line_number}"
          f"\nWrite the name of the stop and then press 'Enter' to add it to the route"
          f"\nNames will be added according to the order inserted"
          f"\nNumbers and Special Characters are not allowed (except whitespace)"
          f"\nTo stop write 'endlist' and press 'Enter'"
          f"\nTo abort write 'abortlist' and press 'Enter'\n")
    while new_stop.lower() != "endlist" and new_stop.lower() != "abortlist":
        new_stop = input(f"Enter stop number {stop_number}: ")
        if not new_stop.replace(' ', '').isalpha() or new_stop == "":
            raise NotStopName(new_stop)
        elif new_stop.lower() != "endlist" and new_stop.lower() != "abortlist":
            new_list_of_stops.append(new_stop)
            stop_number += 1
    match new_stop.lower():
        case "endlist":
            if not new_list_of_stops:
                raise EmptyListOfStops()
            return new_list_of_stops
        case "abortlist":
            raise ListOfStopsAborted()


def manager_update_type() -> int:
    update_type = input("Select update type:\n1) Update Origin\n2) Update Destination\n3) Update entire Route"
                        "\n\nEnter selection: ")
    print("")
    if update_type.isnumeric() and update_type in {'1', '2', '3'}:
        return int(update_type)
    else:
        raise InvalidUserInput(update_type)


def verify_driver_name() -> str:
    driver_name = input(f"Please enter driver name (No numbers or Special Characters): ")
    print("")
    if driver_name.replace(' ', '').isalpha():
        return driver_name
    raise NotDriverName(driver_name)


def verify_time(time_type: str) -> datetime.time:
    receiving_input = True
    while receiving_input:
        correct = False
        hours = input(f"Enter {time_type} hour in 24H Format (##): ")
        minutes = input(f"Enter {time_type} minutes (##): ")
        if not hours.isnumeric() or not minutes.isnumeric():
            print("Invalid input - Please only enter numbers"
                  "\nExample for a valid time format: 09:05"
                  "\nPlease try again\n")
        else:
            while not correct:
                print(f"Confirm your input -> {hours}:{minutes}")
                verify_correct = input("Enter 'Y' to confirm or 'N' to re-enter: ")
                if verify_correct.lower() == 'y' or verify_correct.lower() == 'yes':
                    correct = True
                    receiving_input = False
                elif verify_correct.lower() == 'n' or verify_correct.lower() == 'no':
                    correct = True
                else:
                    print("Please only enter 'Y' or 'N'")
    try:
        temp_datetime = datetime.datetime.strptime(':'.join([hours, minutes]), "%H:%M")
    except ValueError:
        raise WrongTimeFormat(time_type)
    return temp_datetime.time()
