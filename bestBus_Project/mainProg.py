# Best Bus Ever - Main Program
import os.path
import pickle
from frontend.general_mainMenu_utils import *
from frontend.client_mainMenu_utils import *
from frontend.manager_mainMenu_utils import *
from backend.bestBusEver import *


if __name__ == "__main__":
    # Variable Initialization
    if not os.path.exists("bestBus.pickle"):
        bestBus = BestBusCompany()
    else:
        with open("bestBus.pickle", 'rb') as f:
            bestBus = pickle.load(f)
    client_log_in = False
    manager_log_in = False
    program_run = True
    print_ascii_art()  # Show Welcome Art + Message
    while program_run:  # General main_menu:
        user_choice = None
        try:
            user_choice = general_main_menu_display_msg()  # Ask for user definition (client/manager) or Quit Program
        except InvalidUserInput as e:
            print(e)
        match user_choice:
            case 1:  # For client -> move to client main menu
                client_log_in = True
            case 2:  # For manager -> Ask for password -> move to manager main menu
                if verify_manager_password():
                    manager_log_in = True
                else:
                    print("Out of Login attempts\nExiting program...")
                    program_run = False
            case 3:  # For Quit Program -> verify selection -> Terminate program run
                if verify_terminate_program():
                    program_run = False
            case _:
                print("Please try again")

    # Client main_menu:
        while client_log_in:
            client_choice = None
            search_type = None
            try:
                client_choice = client_main_menu_display_msg()  # Ask for action (Search route / Report delay / Display all routes / Logout)
            except InvalidUserInput as e_invalid_client_choice:
                print(e_invalid_client_choice)
                print("Enter only numbers from the menu")
            match client_choice:
                case 1:  # Search for a route
                    try:
                        search_type = client_search_by()  # Ask for type of search
                    except InvalidUserInput as e_invalid_search_type:
                        print(e_invalid_search_type)
                        print("Enter only numbers from the menu")
                    match search_type:
                        case 1:  # Search by Line number
                            try:
                                client_line_number = verify_line_number()
                                found_route_list = bestBus.search_route_by_line_number(client_line_number)
                                print("Search Results: ")
                                for route in found_route_list:
                                    print(route)
                            except NotNumber as e_number:
                                print(e_number)
                            except LineNotExists as e_line_not_exist:
                                print(e_line_not_exist)
                            finally:
                                input("\nPress Enter to continue...")
                        case 2:  # Search by Origin
                            try:
                                client_origin_stop = verify_stop_name("origin")
                                found_route_list = bestBus.search_route_by_origin_stop(client_origin_stop)
                                print("Search Results: ")
                                for route in found_route_list:
                                    print(route)
                            except NotStopName as e_not_stop_name:
                                print(e_not_stop_name)
                            except OriginNotExists as e_origin_not_exists:
                                print(e_origin_not_exists)
                            finally:
                                input("\nPress Enter to continue...")
                        case 3:  # Search by Destination
                            try:
                                client_destination_stop = verify_stop_name("destination")
                                found_route_list = bestBus.search_route_by_destination_stop(client_destination_stop)
                                print("Search Results: ")
                                for route in found_route_list:
                                    print(route)
                            except NotStopName as e_not_stop_name:
                                print(e_not_stop_name)
                            except DestinationNotExists as e_destination_not_exists:
                                print(e_destination_not_exists)
                            finally:
                                input("\nPress Enter to continue...")
                        case 4:  # Search by Stop along the way
                            try:
                                client_stop = verify_stop_name("stop")
                                found_route_list = bestBus.search_route_by_any_stop(client_stop)
                                print("Search Results: ")
                                for route in found_route_list:
                                    print(route)
                            except NotStopName as e_not_stop_name:
                                print(e_not_stop_name)
                            except StopNotExists as e_stop_not_exists:
                                print(e_stop_not_exists)
                            finally:
                                input("\nPress Enter to continue...",)
                        case _:
                            print("Please try again")
                case 2:  # Report a delay in a Route's Scheduled Ride
                    try:
                        line_scheduled_rides_ids = []
                        client_line_number = verify_line_number()
                        found_route_list = bestBus.search_route_by_line_number(client_line_number)
                        print(f"Line {client_line_number} Scheduled Rides: ")
                        for scheduled_ride in found_route_list[0].get_scheduled_rides():
                            print(scheduled_ride)
                            line_scheduled_rides_ids.append(scheduled_ride.get_ride_id())
                        client_delayed_ride_id = verify_delayed_ride_id(line_scheduled_rides_ids)
                        bestBus.report_delay(client_line_number, client_delayed_ride_id)
                    except NotNumber as e_number:
                        print(e_number)
                    except LineNotExists as e_line_not_exist:
                        print(e_line_not_exist)
                    except InvalidDelayedRideID as e_invalid_delayed_ride_id:
                        print(e_invalid_delayed_ride_id)
                    except RideNotExists as e_ride_not_exist:
                        print(e_ride_not_exist)
                    finally:
                        input("\nPress Enter to continue...")
                case 3:  # Display all routes
                    for route in bestBus.get_all_routes():
                        print(route, end="\n\n")
                case 4:  # Logout
                    if verify_logout():
                        client_log_in = False  # Once Logout is verified return to General main_menu
                case _:
                    print("Please try again")

    # Manager main_menu:
        while manager_log_in:
            manager_choice = None
            update_type = None
            try:
                manager_choice = manager_main_menu_display_msg()  # Ask for action (Add route / Delete route / Update route / Add scheduled ride to route / Logout)
            except InvalidUserInput as e_invalid_manager_choice:
                print(e_invalid_manager_choice)
                print("Enter only numbers from the menu")
            match manager_choice:
                case 1:  # Add a new route
                    try:
                        new_line_number = verify_line_number()
                        new_list_of_stops = create_list_of_stops(new_line_number)
                        bestBus.add_route(new_line_number, new_list_of_stops)
                    except NotNumber as e_number:
                        print(e_number)
                    except NotStopName as e_not_stop_name:
                        print(e_not_stop_name)
                    except LineAlreadyExists as e_line_already_exists:
                        print(e_line_already_exists)
                    except ListOfStopsAborted as e_list_creation_aborted:
                        print(e_list_creation_aborted)
                    except EmptyListOfStops as e_empty_list_of_stops:
                        print(e_empty_list_of_stops)
                case 2:  # Delete an existing route
                    try:
                        line_number_to_delete = verify_line_number()
                        bestBus.delete_route(line_number_to_delete)
                    except NotNumber as e_number:
                        print(e_number)
                    except LineNotExists as e_line_not_exist:
                        print(e_line_not_exist)
                case 3:  # Update an existing route
                    try:
                        update_line_number = verify_line_number()
                        update_type = manager_update_type()
                    except NotNumber as e_number:
                        print(e_number)
                    except InvalidUserInput as e_invalid_update_type_choice:
                        print(e_invalid_update_type_choice)
                    match update_type:
                        case 1:  # Update Origin stop
                            try:
                                new_origin_stop = verify_stop_name("origin")
                                bestBus.update_origin_stop(update_line_number, new_origin_stop)
                            except NotStopName as e_not_stop_name:
                                print(e_not_stop_name)
                            except LineNotExists as e_line_not_exist:
                                print(e_line_not_exist)
                        case 2:  # Update Destination stop
                            try:
                                new_destination_stop = verify_stop_name("destination")
                                bestBus.update_destination_stop(update_line_number, new_destination_stop)
                            except NotStopName as e_not_stop_name:
                                print(e_not_stop_name)
                            except LineNotExists as e_line_not_exist:
                                print(e_line_not_exist)
                        case 3:  # Update entire List of Stops
                            try:
                                updated_list_of_stops = create_list_of_stops(update_line_number)
                                bestBus.update_list_of_stops(update_line_number, updated_list_of_stops)
                            except NotStopName as e_not_stop_name:
                                print(e_not_stop_name)
                            except ListOfStopsAborted as e_list_creation_aborted:
                                print(e_list_creation_aborted)
                            except LineNotExists as e_line_not_exist:
                                print(e_line_not_exist)
                            except TypeError as e_type_error:
                                print("Invalid new List of Stops")
                        case _:
                            print("Please try again")
                case 4:  # Add scheduled ride to route
                    try:
                        line_number_to_add_ride = verify_line_number()
                        list_of_scheduled_rides = bestBus.get_line_existing_rides_list(line_number_to_add_ride)
                        print(f"Line {line_number_to_add_ride} existing rides list:")
                        for ride in list_of_scheduled_rides:
                            print(ride)
                        driver_name = verify_driver_name()
                        origin_time = verify_time("origin")
                        destination_time = verify_time("destination")
                        bestBus.add_scheduled_ride_to_line(line_number_to_add_ride, origin_time, destination_time, driver_name)
                    except NotNumber as e_number:
                        print(e_number)
                    except LineNotExists as e_line_not_exist:
                        print(e_line_not_exist)
                    except NotDriverName as e_not_driver_name:
                        print(e_not_driver_name)
                    except WrongTimeFormat as e_wrong_time_format:
                        print(e_wrong_time_format)
                    except TypeError as e_type_error:
                        print("Something went wrong while creating a new Scheduled Ride")
                case 5:  # Logout
                    if verify_logout():
                        manager_log_in = False  # Once Logout is verified return to General main_menu
                case _:
                    print("Please try again")

    # After program exits:
    print("Thank you for using Best-Bus!\nHope to see you again")
    with open("bestBus.pickle", 'wb') as f:
        pickle.dump(bestBus, f)
