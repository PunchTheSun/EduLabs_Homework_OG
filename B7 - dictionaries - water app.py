# B7 - dictionaries - water app

def sign_up(user_dict: dict) -> None:
    username = input("Enter a username: ")
    user_dict[username] = {"dates":{}}
    return

def add_glasses(user_dict: dict) -> None:
    found = False
    username = input("Enter a username: ")
    for names in user_dict.keys():
        if username.lower() == names.lower():
            found = True
    if not found:
        print("Invalid username, Not in database")
        return

    while True:
        new_glasses = input("Enter amount of glasses you drank: ")
        if new_glasses.isnumeric():
            new_glasses = int(new_glasses)
            break
        else:
            print("Please enter a number, Try again")

    new_date = input("Enter the date (DD-MM-YYYY): ")
    if user_dict.get(username).get("dates").get(new_date, "Not Found") != "Not Found":
        current_glasses = user_dict[username]["dates"][new_date]
        new_glasses += current_glasses
    user_dict[username]["dates"][new_date] = new_glasses
    return

def display_date_glasses(user_dict: dict, username: str, date: str) -> None:
    user_found = False
    date_found = False

    for names in user_dict.keys():
        if names.lower() == username.lower():
            user_found = True
    if not user_found:
        print("Invalid username, Not in database")
        return

    for dates in user_dict[username]["dates"].keys():
        if dates.lower() == date.lower():
            date_found = True
    if not date_found:
        print(f"No information for the date: {date}")
        return

    print(f'On the date: {date} you have drank: {user_dict[username]["dates"][date.lower()]} glasses of water.')
    return

def total_glasses(user_dict: dict) -> int:
    all_glasses = 0
    for username in user_dict.keys():
        for dates in user_dict[username]["dates"]:
                all_glasses += user_dict[username]["dates"][dates]
    return all_glasses

def user_total_glasses(user_dict: dict) -> str:
    user_glasses = 0
    found = False
    username = input("Enter username: ")
    for names in user_dict.keys():
        if username.lower() == names.lower():
            found = True
    if not found:
        return "Invalid username, Not in database"

    for dates in user_dict[username]["dates"]:
        user_glasses += user_dict[username]["dates"][dates]
    return print(f"The total amount of glasses for {username} is: {user_glasses}")



# Main Code

users_dict = {}
choice = ""
while True:
    choice = input("1. Signup\n2. Add\n3. Display\n4. Display Total Glasses in database\n5. Display Specific User Total Glasses\n6. Exit\nWhat would you like to do (1 / 2 / 3 / 4 / 5 / 6): ")
    match choice:
        case "1":
            sign_up(users_dict)
        case "2":
            add_glasses(users_dict)
        case "3":
            username_display = input("Enter a username to display: ")
            date_display = input("Enter a date to display (DD-MM-YYYY): ")
            display_date_glasses(users_dict,username_display,date_display)
        case "4":
            print(f"The total glasses number in the database is: {total_glasses(users_dict)}")
        case "5":
            user_total_glasses(users_dict)
        case "6":
            break
        case _:
            print("Invalid input, Please enter a number from the menu to specify your selection")