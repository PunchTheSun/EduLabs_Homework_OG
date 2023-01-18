## A11-coffee - if stmts, loops, lists
coffee_list_unchanged = ["Espresso","Doppio","Lungo","Ristretto","Macchiato","Corretto","Con Panna","Romano","Cappucino","Americano","Cafe Latte","Flat White","Marocchino","Mocha","Bicerin","Breve","Raf Coffee","Mead Raf","Vienna Coffe","Chocolate Milk","Latte Macchiato","Glace","Freddo","Irish Coffee","Frappe","Cappuccino Freddo","Caramel Frappe","Espresso Laccino"]
coffee_list = ["Espresso","Doppio","Lungo","Ristretto","Macchiato","Corretto","Con Panna","Romano","Cappucino","Americano","Cafe Latte","Flat White","Marocchino","Mocha","Bicerin","Breve","Raf Coffee","Mead Raf","Vienna Coffe","Chocolate Milk","Latte Macchiato","Glace","Freddo","Irish Coffee","Frappe","Cappuccino Freddo","Caramel Frappe","Espresso Laccino"]
print("Welcome to 'CoffeeMaster9000' Glad to have you drinking with us today.")
excluded_numbers = []
temp_val = None


## User input - Time (HH:MM)
time = input("Enter current time of day (HH:MM): ")
hours_minutes = time.split(":")
if not hours_minutes[0].isnumeric() or not hours_minutes[-1].isnumeric() or len(hours_minutes)>2:
    print("Invalid input\nPlease Enter a correct time in the following format:\nHH:MM\nPlease try again.")
    exit(1)
hours = int(hours_minutes[0])
minutes = int(hours_minutes[1])
if hours > 23 or minutes > 59:
    print("Invalid input\nPlease enter a real time (00:00 up to 23:59)\nPlease Enter a correct time in the following format:\nHH:MM\nPlease try again.")
    exit(1)


## User input - Number of people drinking
friends = input("Enter the total number of people that will be drinking: ")
if not friends.isnumeric():
    print("Invalid input\nPlease Enter numbers only\nPlease try again.")
    exit(1)
friends = int(friends)


## User input - Starting number
starting_number = input("Enter a number (Over 0): ")
if not starting_number.isnumeric():
    print("Invalid input\nPlease Enter numbers only\nPlease try again.")
    exit(1)
starting_number = int(starting_number)

## Option - A: WITH EXCLUDED COFFEE TYPES OPTION
## User input - Excluded numbers
temp_val = input("Enter 'Y' if there are any coffee types you dislike: ")
if temp_val == "Y" or temp_val == "y":
    print('Please enter disliked coffee types numbers (Enter "C" to stop): ')
    while True:
        temp_val = input()
        if temp_val == "C" or temp_val == "c":
            break
        if not temp_val.isnumeric():
            print("Invalid input, Please enter a number or 'C' to stop")
        else:
            excluded_numbers.append(int(temp_val))
    for i, disliked_type in enumerate(excluded_numbers):
        coffee_list.pop(disliked_type-1-i)
## Calculations and output
for friend_num in range(0,friends):
    friend_choice = coffee_list[((hours+(starting_number*friend_num))%(28-len(excluded_numbers)))-1]
    print(f"Drinker #{friend_num+1}: Coffee #{coffee_list_unchanged.index(friend_choice)+1} - {friend_choice}")


## Option - B: Calculations and output - WITHOUT EXCLUDED COFFEE TYPES OPTION
# for friend_num in range(0,friends):
#     friend_choice = coffee_list[((hours+(starting_number*friend_num))%28)-1]
#     print(f"Drinker #{friend_num+1}: Coffee #{(hours+(starting_number*friend_num))%28} - {friend_choice}")