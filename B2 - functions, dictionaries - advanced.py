# B2 - functions, dictionaries - advanced

# Ex1

# def drop_empty_none(func_dict: dict, inplace = False) -> None | dict:
#     if inplace:
#         main_keys = []
#         for key in func_dict.keys():
#             if func_dict[key] == "None" or func_dict[key] == "" or func_dict[key] == None or func_dict.get(key) == []:
#                 main_keys.append(key)
#         for del_key in main_keys:
#             main_dict.pop(del_key)
#         return
#     else:
#         ret_dict = {}
#         for key in func_dict.keys():
#             if func_dict[key] != "None" and func_dict[key] != "" and func_dict[key] != None and func_dict.get(key) != []:
#                 ret_dict[key] = func_dict.get(key)
#         return ret_dict
#
# # Main Code - Ex1
#
# main_dict = {'c1': 'Red', 'c2': 'Green', 'c3': None, 'c4': [], 'c5': ""}
# print(drop_empty_none(main_dict))
# main_dict["c6"] = "Blue"
# drop_empty_none(main_dict,True)
# print(main_dict)


# Ex2

# def group_up(my_list: list) -> dict:
#     ret_dict = {}
#     for temp_key, temp_val in my_list:
#         if temp_key in ret_dict.keys():
#             ret_dict[temp_key] = (f"{ret_dict[temp_key]}, {temp_val}")
#         else:
#             ret_dict[temp_key] = temp_val
#     return ret_dict
#
# # Main Code - Ex2
#
# original_list = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1),('blue',7)]
# print(group_up(original_list))


# Ex3
# def split_up(my_dict: dict) -> list:
#     ret_list = []
#     temp_keys = list(my_dict.keys())
#     temp_values = list(my_dict.values())
#     for i in range(0,len(temp_keys)-1):
#         for j, val in enumerate(temp_values[i]):
#             ret_list.append({temp_keys[i]:val, temp_keys[i+1]:temp_values[i+1][j]})
#     return ret_list
#
#
#
# # Main Code - Ex3
# original_dict = {'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
# print(split_up(original_dict))