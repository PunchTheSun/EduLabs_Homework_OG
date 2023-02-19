import pytz
from frontend.menu_utils import *
from backend.api_utils import get_nationalize_data
from backend.api_utils import get_countryrest_data

if __name__ == "__main__":
    user_choice = 'y'
    username = None
    invalid_name_input = True
    invalid_continue_input = True
    while user_choice == 'y':
        while invalid_name_input:
            try:
                username = get_name()
                invalid_name_input = False
            except NameError as e_invalid_input:
                print("Invalid input, Please only enter letters and whitespaces")
                invalid_name_input = True
            except ValueError as e_invalid_input:
                print("Invalid input, Whitespaces aren't allowed")
                invalid_name_input = True
        nationalize_data = get_nationalize_data(username)
        countryRest_data = get_countryrest_data(nationalize_data['country'][0]['country_id'])
        country_name = countryRest_data[0]["name"]["common"]
        continent_name = countryRest_data[0]["region"]
        sub_region_name = countryRest_data[0]["subregion"]
        languages_name_list = countryRest_data[0]["languages"]
        country_timezone_name_list = countryRest_data[0]["timezones"]
        print(nationalize_data)
        print(countryRest_data)
        print("")
        print(f"User is probably from: {country_name}")
        print(f"{country_name} is located in {continent_name}")
        if len(languages_name_list) == 1:
            print(f"Language name: {languages_name_list[0]}")
        elif len(languages_name_list) > 1:
            print("The country's languages: ")
            for language in languages_name_list:
                print(language)
        if len(country_timezone_name_list) == 1:
            print(f"Timezone name: {country_timezone_name_list[0]}")
        elif len(country_timezone_name_list) > 1:
            print("The country's timezones: ")
            for timezone in country_timezone_name_list:
                print(timezone)
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
