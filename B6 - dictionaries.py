# B6 - dictionaries

# Ex1
#
# stocks_data = {
#     "TSLA" : {
#         "company_name":"Tesla",
#         "employee_num":300,
#         "address":"Google City 25",
#         "ceo_name":"Elon Musk",
#         "dates":{
#             "01-01-2023": {
#                 "open_price":500,
#                 "close_price":150,
#                 "volume":6000000
#             },
#             "02-01-2023": {
#                 "open_price": 150,
#                 "close_price": 100,
#                 "volume": 350000
#             },
#             "03-01-2023": {
#                 "open_price": 100,
#                 "close_price": 85,
#                 "volume": 2000000
#             }
#         }
#
#     },
# "WAZE" : {
#         "company_name":"Waze",
#         "employee_num":100,
#         "address":"Google City 20",
#         "ceo_name":"Someone Somebody",
#         "dates":{
#             "01-01-2023": {
#                 "open_price":1000,
#                 "close_price":1500,
#                 "volume":8600000
#             },
#             "02-01-2023": {
#                 "open_price": 1500,
#                 "close_price": 2000,
#                 "volume": 400000
#             },
#             "03-01-2023": {
#                 "open_price": 2000,
#                 "close_price": 1800,
#                 "volume": 3000000
#             }
#         }
#
#     }
# }

# Main Code - Ex1
# while True:
#     company = input("Enter stock ticker to present information (or 'Exit' to stop): ")
#     if company.lower() == "exit":
#         break
#     ticker_exist = False
#     for key in stocks_data.keys():
#         if key.lower() == company.lower():
#             ticker_exist = True
#     if ticker_exist:
#         print(f"Company name: {stocks_data[company]['company_name']}\nNumber of employees: {stocks_data[company]['employee_num']}\nAddress: {stocks_data[company]['address']}\nCEO Name: {stocks_data[company]['ceo_name']}")
#         print(f"Stock information ordered by dates:")
#         for date in stocks_data.get(company).get("dates").keys():
#             print(f"Date: {date}\nOpening price: {stocks_data[company]['dates'][date]['open_price']}\nClose price: {stocks_data[company]['dates'][date]['close_price']}\nVolume: {stocks_data[company]['dates'][date]['volume']}")
#     else:
#         print("Invalid input, stock ticker isn't in database")


# Ex2

# def insert_bday(my_dict: dict[str]) -> dict | None:
#     name = input("Enter a name: ")
#     override = False
#     choice = ""
#     for names in my_dict.keys():
#         if name.lower() == names.lower():
#             override = True
#     if override:
#         while True:
#             choice = input(f"{name} already exists in the database, Would you like to override it? (Y/N): ")
#             if choice.lower() == "n":
#                 return {name:my_dict.get(name)}
#             elif choice.lower() == "y":
#                 bday = input("Enter your birthday (DD/MM/YYYY): ")
#                 return {name:bday}
#             else:
#                 print("Invalid input.")
#     bday = input("Enter your birthday (DD/MM/YYYY): ")
#     return {name:bday}
#
# def lookup_bday(my_dict: dict[str]) -> str | None:
#     name = input("Enter a name to search: ")
#     is_found = False
#     name_suggestions = []
#     for names in my_dict.keys():
#         if names.lower() == name.lower():
#             is_found = True
#     if is_found:
#         return my_dict.get(name)
#     for names in my_dict.keys():
#         if name.lower() in names.lower():
#             name_suggestions.append(names)
#     print(f"We have: {name_suggestions[::]}\nPlease insert a name from the list above or '$$$' to return to the main menu (Case sensitive):")
#     suggestion_choice = input()
#     if suggestion_choice == "$$$":
#         return "Returning to main menu"
#     return my_dict.get(suggestion_choice, "Invalid name, Returning to main menu")

# Main Code - Ex2
# choice = ""
# users_bday = {}
# while choice.lower() != "exit":
#     choice = input("Type a command 'Insert', 'Look Up', 'Exit': ")
#     if choice.lower() == "insert":
#         users_bday.update(insert_bday(users_bday))
#     elif choice.lower() == "look up":
#         print(lookup_bday(users_bday))
#     elif choice.lower() != "exit":
#         print("Wrong input provided, please follow the instructions")

# Ex3
# import pprint
#
# def insert_persons(n: int) -> dict:
#     ret_dict = {}
#     for i in range(1,n+1):
#         one_p_dict = {"id_num": "0", "first_name": "", "last_name": "", "birth_year": "0", "phone_num": ""}
#         print(f"Enter information for person number {i}:")
#         for key_name in one_p_dict.keys():
#             temp_value = input(f"Enter {key_name}: ")
#             one_p_dict[key_name] = temp_value
#         ret_dict[one_p_dict["id_num"]] = one_p_dict
#     return ret_dict
#
# # Main Code - Ex3
# persons_num = int(input("Enter a number of persons: "))
# pprint.pprint(insert_persons(persons_num))