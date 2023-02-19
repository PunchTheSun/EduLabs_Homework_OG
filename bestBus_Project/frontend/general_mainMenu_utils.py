# General Main Menu Functions
from frontend.menus_Exceptions import *


def print_ascii_art() -> None:
    print("                          __\n .-----------------------'  |\n/| _ .---. .---. .---. .---.|\n|j||||___| |___| |___| |___||\n|=|||=======================|\n[_|j||(O)\__________|(O)\___]")
    print("Welcome to Best-Bus!")


def general_main_menu_display_msg() -> int:
    choice = input("\n1) Login as Client\n2) Login as Manager\n3) Exit Application\n\nPlease select an option from the menu (1/2/3): ")
    if choice.isnumeric() and choice in {'1', '2', '3'}:
        return int(choice)
    else:
        raise InvalidUserInput(choice)


def verify_terminate_program() -> bool:
    while True:
        user_input = input("Are you sure you want to quit? (Y/N): ")
        if user_input.lower() == "y" or user_input.lower() == "yes":
            verification = True
            break
        elif user_input.lower() == "n" or user_input.lower() == "no":
            verification = False
            break
        else:
            print("Invalid input, Please enter 'Y' or 'N'")
    return verification


def verify_manager_password() -> bool:
    login_tries = 0
    while login_tries < 3:
        user_password = input("Please enter password: ")
        login_tries += 1
        if user_password == "RideWithUs!":
            return True
        else:
            print(f"Wrong password, login attempts left: {3-login_tries}")
    return False


def verify_logout() -> bool:
    while True:
        user_input = input("Are you sure you want to logout? (Y/N): ")
        if user_input.lower() == "y" or user_input.lower() == "yes":
            verification = True
            break
        elif user_input.lower() == "n" or user_input.lower() == "no":
            verification = False
            break
        else:
            print("Invalid input, Please enter 'Y' or 'N'\n")
    return verification


def verify_line_number() -> int:
    line_number = input("Please enter a line number: ")
    if line_number.isnumeric():
        return int(line_number)
    raise NotNumber(line_number)


def verify_stop_name(stop_type: str) -> str:
    stop_name = input(f"Please enter {stop_type} name (No numbers or Special Characters): ")
    print("")
    if stop_name.replace(' ', '').isalpha():
        return stop_name
    raise NotStopName(stop_name)
