import datetime
from frontend.menu_utils import *
from backend.api_utils import get_nationalize_data, get_nationalize_data_multithread, \
    get_nationalize_data_from_file, get_nationalize_data_multithread_from_file

# from backend.api_utils import get_countryrest_data

if __name__ == "__main__":
    user_choice = 'y'
    username10 = None
    invalid_name_input = True
    invalid_continue_input = True
    while user_choice == 'y':
        # while invalid_name_input:
        #     try:
        #         username = get_name()
        #         invalid_name_input = False
        #     except NameError as e_invalid_input:
        #         print("Invalid input, Please only enter letters and whitespaces")
        #         invalid_name_input = True
        #     except ValueError as e_invalid_input:
        #         print("Invalid input, Whitespaces aren't allowed")
        #         invalid_name_input = True
        username10 = ["Or", "John", "Adam", "Muhammad", "Katie", "Cedric", "Daria", "Lee", "Claud", "Charles"]
        username100 = ["Or", "John", "Adam", "Muhammad", "Katie", "Cedric", "Daria", "Lee", "Claud", "Charles",
                       "Or", "John", "Adam", "Muhammad", "Katie", "Cedric", "Daria", "Lee", "Claud", "Charles",
                       "Or", "John", "Adam", "Muhammad", "Katie", "Cedric", "Daria", "Lee", "Claud", "Charles",
                       "Or", "John", "Adam", "Muhammad", "Katie", "Cedric", "Daria", "Lee", "Claud", "Charles",
                       "Or", "John", "Adam", "Muhammad", "Katie", "Cedric", "Daria", "Lee", "Claud", "Charles",
                       "Or", "John", "Adam", "Muhammad", "Katie", "Cedric", "Daria", "Lee", "Claud", "Charles",
                       "Or", "John", "Adam", "Muhammad", "Katie", "Cedric", "Daria", "Lee", "Claud", "Charles",
                       "Or", "John", "Adam", "Muhammad", "Katie", "Cedric", "Daria", "Lee", "Claud", "Charles",
                       "Or", "John", "Adam", "Muhammad", "Katie", "Cedric", "Daria", "Lee", "Claud", "Charles",
                       "Or", "John", "Adam", "Muhammad", "Katie", "Cedric", "Daria", "Lee", "Claud", "Charles"]

        start_time = datetime.datetime.now()
        nationalize_data = get_nationalize_data(username10)
        end_time = datetime.datetime.now()
        print(f"None Multithreaded time for 10 results: {(end_time - start_time).seconds}."
              f"{(end_time - start_time).microseconds}")

        start_time_multithread = datetime.datetime.now()
        nationalize_data_multithread = get_nationalize_data_multithread(username10)
        end_time_multithread = datetime.datetime.now()
        print(f"Multithreaded time for 10 results: {(end_time_multithread - start_time_multithread).seconds}."
              f"{(end_time_multithread - start_time_multithread).microseconds}")

        start_time = datetime.datetime.now()
        nationalize_data_file = get_nationalize_data_from_file("list_of_names.txt")
        end_time = datetime.datetime.now()
        print(f"None Multithreaded time for 100 results to file: {(end_time - start_time).seconds}."
              f"{(end_time - start_time).microseconds}")

        start_time_multithread = datetime.datetime.now()
        nationalize_data_multithread_file = get_nationalize_data_multithread_from_file("list_of_names.txt")
        end_time_multithread = datetime.datetime.now()
        print(
            f"None Multithreaded time for 100 results to file: "
            f"{(end_time_multithread - start_time_multithread).seconds}."
            f"{(end_time_multithread - start_time_multithread).microseconds}")

        # countryRest_data = get_countryrest_data(nationalize_data['country'][0]['country_id'])
        # country_name = countryRest_data[0]["name"]["common"]n

        # continent_name = countryRest_data[0]["region"]
        # sub_region_name = countryRest_data[0]["subregion"]
        # languages_name_list = countryRest_data[0]["languages"]
        # country_timezone_name_list = countryRest_data[0]["timezones"]
        # # print(nationalize_data)
        # # print(countryRest_data)
        # print("")
        # print(f"User is probably from: {country_name}")
        # print(f"{country_name} is located in {continent_name}")
        # if len(languages_name_list) == 1:
        #     print(f"Language name: {languages_name_list[0]}")
        # elif len(languages_name_list) > 1:
        #     print("The country's languages: ")
        #     for language in languages_name_list:
        #         print(language)
        # if len(country_timezone_name_list) == 1:
        #     print(f"Timezone name: {country_timezone_name_list[0]}")
        # elif len(country_timezone_name_list) > 1:
        #     print("The country's timezones: ")
        #     for timezone in country_timezone_name_list:
        #         print(timezone)
        # Can't get the timezones part to work.. Will fix in the future!
        # print(f"The time in {country_name} right now is: ")
        # for timezone in country_timezone_name_list:
        #     print(pytz.timezone(f"{continent_name}/{sub_region_name}"))

        while invalid_continue_input:
            try:
                user_choice = ask_continue()
                invalid_continue_input = False
            except ValueError as e_invalid_input:
                print("Invalid Input, Please only enter 'Y' or 'N'")
                invalid_continue_input = True
        invalid_name_input = True
        invalid_continue_input = True
