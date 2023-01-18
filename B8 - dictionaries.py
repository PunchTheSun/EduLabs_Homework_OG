# B8 - dictionaries

# Ex1
# def list_merger(cars: list, colors: list) -> dict:
#     ret_dict = {}
#     car_exist = False
#     for car, color in zip(cars,colors):
#         for car_check in ret_dict.keys():
#             if car == car_check:
#                 car_exist = True
#         if car_exist:
#             if ret_dict[car] != color:
#                 ret_dict[car] = (f"{color}, {ret_dict[car]}")
#         else:
#             ret_dict[car] = color
#     return ret_dict
#
# # Main Code - Ex1
#
# cars_list = ["Mazda 3",     "Toyota Yaris",     "Volvo S40",    "Mazda 2",  "Toyota Yaris", "Volvo S40"]
# color_list = ["red",         "white",            "red",          "blue",     "black",        "red"]
# print(list_merger(cars_list,color_list))


# Ex2
# def count_strings(text: list[str]) -> dict:
#     ret_dict = {}
#     temp_count = 0
#     for word in text:
#         if word in ret_dict.keys():
#             temp_count = ret_dict[word]
#             temp_count += 1
#             ret_dict[word] = temp_count
#         else:
#             ret_dict[word] = 1
#     return ret_dict
#
#
# # Main Code - Ex2
# string_list = ["sun", "water", "air", "water", "water", "apple", "air"]
# print(count_strings(string_list))


# Ex3
# def no_idea_for_function_name(dates: list, stocks: list) -> list[dict]:
#     date_key = {}
#     stock_key = {}
#     temp_val = None
#
#     for i in range(0,len(dates)):
#         if dates[i] in date_key.keys():
#             date_key[dates[i]] = (f"{date_key[dates[i]]}, {stocks[i]}")
#         else:
#             date_key[dates[i]] = stocks[i]
#
#         if stocks[i] in stock_key.keys():
#             stock_key[stocks[i]] = (f"{stock_key[stocks[i]]}, {dates[i]}")
#         else:
#             stock_key[stocks[i]] = dates[i]
#
#     return [date_key,stock_key]
#
#
#
# # Main Code - Ex3
#
# import pprint
#
# date_list = ["11-05-22", "12-05-22", "13-05-22", "12-05-22", "11-05-22", "11-05-22"]
# stock_list = ["TSLA", "TSLA", "AAPL", "MSFT", "AAPL", "IBM"]
#
# pprint.pprint(no_idea_for_function_name(date_list,stock_list))