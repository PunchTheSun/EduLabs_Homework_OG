# B5 - List. Dictionary. Set

# B5.1
# def zip_up(list1: list, list2: list) -> dict:
#     ret_dict = {}
#     for item1, item2 in zip(list1, list2):
#         if item1 in ret_dict.keys():
#             ret_dict[item1] = f"{ret_dict[item1]}, {item2}"
#         else:
#             ret_dict[item1] = item2
#     return ret_dict
#
# # Main Code - B5.1:
# flowers = ['Rose','Lily','Tulip','Orchid','Carnation', 'Hyacinth', 'Rose']
# color = ['red', 'white', 'blue','white', 'pink', 'purple', 'white']
# print(zip_up(flowers,color))


# B5.2
# def unique_func(my_list: list[str]) -> set:
#     ret_set = set()
#     for val in my_list:
#         ret_set.add(val.lower())
#     return ret_set
#
#
# # Main Code - B5.2
# colors_2 = ['red', 'White', 'BLUE','white', 'Red', 'sky blue', 'purple', 'orange with white straps']
# print(unique_func(colors_2))


# B5.3
# def intersect_two(l1: list[str], l2: list[str]) -> set:
#     temp_set1 = set()
#     temp_set2 = set()
#     for val1 in l1:
#         temp_set1.add(val1.lower())
#     for val2 in l2:
#         temp_set2.add(val2.lower())
#     ret_set = temp_set1.intersection(temp_set2)
#     return ret_set
#
#
# # Main Code - B5.3
# color_1 = ['red', 'white', 'blue','white', 'pink', 'purple', 'white']
# colors_2 = ['red', 'White', 'BLUE','white & Red', 'sky blue', 'purple', 'orange with white straps']
# print(intersect_two(color_1,colors_2))


# B5.4
# def derived_colors(list_basic: list[str], l1: list[str], l2: list[str]) -> set:
#     ret_set = set()
#     for val1 in l1:
#         for basic_val in list_basic:
#             if basic_val.lower() in val1.lower():
#                 ret_set.add(val1.lower())
#     for val2 in l2:
#         for basic_val in list_basic:
#             if basic_val.lower() in val2.lower():
#                 ret_set.add(val2.lower())
#     return ret_set
#
# # Main Code - B5.4
# colors_0 = ['red', 'blue', 'Purple','white']
# colors_1 = ['orange red', 'blue navy', 'BLUE pure','snow white', 'sky blue', 'pure purple', 'white cream', 'Eggshell white','donald duck','Orchid purple', 'Medium blue', 'Egyptian blue', 'Neon blue']
# colors_2 = ['red Crimson', 'Liberty blue', 'Purple pizzazz','white & Red', 'sky blue', 'Pale purple', 'Orchid purple', 'BLUE pure','orange']
# print(derived_colors(colors_0,colors_1,colors_2))


# B5.5

# def visited_cities(cities: dict) -> set:
#     ret_set = set()
#     for key in cities.keys():
#         for country in cities[key]:
#             for city in cities[key][country]:
#                 ret_set.add(city.lower())
#     return ret_set
#
# # Main Code - B5.5
# my_cities = {
#    2008:{'Germany':['Berlin', 'Munich'],
#            'France' :['Paris','Leon','Bordeaux']},
#    2009: {'China':['Hong Kong', 'Shanghai','Beijing'],
#             'Japan':['Nagoya','Toyokawa','Yatomi'],
#             'Mexico':['Tijuana','Ecatepec']},
#    2010: {'Germany': ['Berlin', 'Dusseldorf'],
#             'France': ['Paris', 'Nice', 'Bordeaux'],
#             'Japan':['Tokyo','Toyokawa','Yatomi']}
# }
# print(visited_cities(my_cities))


# B5.6
# def visit_dates(cities_dict: dict) -> dict:
#     ret_dict = {}
#     for year in cities_dict.keys():
#         for country in cities_dict[year]:
#             for city in cities_dict[year][country]:
#                 if city in ret_dict.keys():
#                     ret_dict[city] = (f"{ret_dict[city]}, {year}")
#                 else:
#                     ret_dict[city] = year
#     return ret_dict
#
#
# # Main Code - B5.6
# my_cities = {
#    2008:{'Germany':['Berlin', 'Munich'],
#            'France' :['Paris','Leon','Bordeaux']},
#    2009: {'China':['Hong Kong', 'Shanghai','Beijing'],
#             'Japan':['Nagoya','Toyokawa','Yatomi'],
#             'Mexico':['Tijuana','Ecatepec']},
#    2010: {'Germany': ['Berlin', 'Dusseldorf'],
#             'France': ['Paris', 'Nice', 'Bordeaux'],
#             'Japan':['Tokyo','Toyokawa','Yatomi']}
# }
#
# print(visit_dates(my_cities))


# B5.7

# def distinct_val(l1: list[str], l2: list[str]) -> set:
#     ret_set = set()
#     s1 = set()
#     s2 = set()
#     for val1 in l1:
#         s1.add(val1.lower())
#     for val2 in l2:
#         s2.add(val2.lower())
#     ret_set = s1.difference(s2)
#     return ret_set
#
# # Main Code - B5.7
# colors_1 = ['orange red','banana', 'blue navy', 'BLUE pure','snow white', 'sky blue', 'pure purple', 'white cream', 'Eggshell white','Orchid purple', 'Medium blue', 'Egyptian blue', 'Neon blue']
# colors_2 = ['red Crimson','banAna1','banana1' ,'Liberty blue', 'Purple pizzazz','white & Red', 'sky blue', 'Pale purple', 'Orchid purple', 'BLUE pure']
# print(distinct_val(colors_1,colors_2))


# B5.8
## I Am assuming all inputs are valid and no need for input validation checks
## It is possible to write over existing catalog entries as question did not specify it had to be avoided
## Question only referred to "new vehicle" therefor ignoring the overwriting of existing elements
# def volvo_catalog(curr_cat: dict) -> dict:
#     new_type = input("Enter new car type (private / semi): ")
#     new_model = input("Enter new car model: ")
#     new_prod_year = int(input("Enter new car production year: "))
#     new_motor = input("Enter new car motor type (Diesel / Patrol / Electric / Hydrogen): ")
#     new_colors = []
#     while True:
#         temp_color = input("Enter new car colors (Enter $$$ to stop): ")
#         if temp_color == "$$$":
#             break
#         new_colors.append(temp_color)
#     curr_cat["type"][new_type][new_model] = {"prod_year":new_prod_year,"motor_type":new_motor,"colors":new_colors}
#     print("New model listed into catalog")
#     return curr_cat
#
#
# # Main Code - B5.8
# import pprint
#
# catalog = {
#     "type":
#         {
#             "private":
#                 {
#                 "S-30":
#                       {
#                           "prod_year":1930,
#                           "motor_type":"Diesel",
#                           "colors":["Orange","Green","Violet"]
#                       }
#                 ,
#                 "S-40":
#                      {
#                           "prod_year":1940,
#                           "motor_type":"Diesel",
#                           "colors":["Orange","Green","Violet","Red-Orange"]
#                       }
#                 ,
#                 "S-60":
#                      {
#                           "prod_year":1960,
#                           "motor_type":"Patrol",
#                           "colors":["Orange","Green","Violet"]
#                       }
#                 ,
#             "S-80":
#                      {
#                           "prod_year":1980,
#                           "motor_type":"Patrol",
#                           "colors":["Orange","Green","Violet","Blue-Violet"]
#                       }
#             ,
#             "S-90":
#                      {
#                           "prod_year":1990,
#                           "motor_type":"Electric",
#                           "colors":["Orange","Green","Violet","Yellow-Green"]
#                       }
#
#         },
#         "semi":
#             {
#              "Vnl-760":
#                     {
#                         "prod_year": 1960,
#                         "motor_type": "Diesel",
#                         "colors": ["Orange", "Green", "Violet"]
#                     }
#                 ,
#                 "Vnl-860":
#                     {
#                         "prod_year": 1960,
#                         "motor_type": "Diesel",
#                         "colors": ["Orange", "Green", "Violet", "Red-Orange"]
#                     }
#                ,
#                 "Vnr-300":
#                     {
#                         "prod_year": 2000,
#                         "motor_type": "Electric",
#                         "colors": ["Orange", "Green", "Violet"]
#                     }
#                 ,
#                 "Vnr-600":
#                     {
#                         "prod_year": 2020,
#                         "motor_type": "Hydrogen",
#                         "colors": ["Orange", "Green", "Violet", "Blue-Violet"]
#                     }
#                 ,
#                 "Vhd-500":
#                     {
#                         "prod_year": 2022,
#                         "motor_type": "Electric",
#                         "colors": ["Orange", "Green", "Violet", "Yellow-Green"]
#                     }
#                 ,
#                 "Vhd-900":
#                     {
#                         "prod_year": 2023,
#                         "motor_type": "Patrol",
#                         "colors": ["Orange", "Green", "Violet", "Yellow-Green"]
#                     }
#
#         }
#     }
# }
#
# while True:
#     choice = input("1. Insert new model\n2. Display catalog\n3. Exit\nEnter a command (1 / 2 / 3): ")
#     match choice:
#         case "1":
#             catalog.update(volvo_catalog(catalog))
#         case "2":
#             pprint.pprint(catalog)
#         case "3":
#             break