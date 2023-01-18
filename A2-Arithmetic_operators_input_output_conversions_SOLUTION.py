# A2-Arithmetic operators, input, output, conversions

# Ex1
# height = int(input("Please enter rectangle's height: "))
# width = int(input("Please enter rectangle's width: "))
# print(f"The rectangle's area is: {height * width}")

# Ex2
# tempC = int(input("\n\nPlease enter the temperature to convert (Celsius): "))
# print(f"The temperature is: {tempC * 1.8} degrees Fahrenheit")

# Ex3
# num1 = int(input("\n\nEnter the first number: "))
# num2 = int(input("Enter the second number: "))
# print(f"Addition result is: {num1 + num2}")
# print(f"Multiplication result is: {num1 * num2}")

# Ex4
# birth_year = int(input("Enter your birth year: "))
# print(f"You are {2022-birth_year} years old.")

# Ex5
# num = int(input("Enter a number: "))
# if num % 2 == 0:
#     print("EVEN")
# else:
#     print("ODD")

# Ex6
# num1 = int(input("Enter the 1st number: "))
# num2 = int(input("Enter the 2nd number: "))
# print(f"{num1} can be divided {num1 // num2} times by {num2} without leftover")

# Ex7
# num = int(input("Enter a 4 digit number: "))
# left_digit = num // 1000
# right_digit = num % 10
# print(f"Left-most digit is: {left_digit}")
# print(f"Right-most digit is: {right_digit}")

# Ex8
# salary = int(input("Bob please insert your salary: "))
# print(f"This month donation is: {salary * 0.14}")

# Ex9
# current_sal = int(input("Insert current salary: "))
# new_sal = int(input("Insert new salary: "))
# print(f"“If you take the new job, you will earn {new_sal - current_sal} more (or less if negative) per year.")

# Ex10
# total_minutes = int(input("Enter amount of minutes in the movie: "))
# hours = total_minutes // 60
# minutes = total_minutes % 60
# print(f"{hours}:{minutes}")

# Ex11
# total_seconds = int(input("Enter amount of seconds in the movie: "))
# hours = total_seconds // 3600
# minutes = (total_seconds // 60) - hours * 60
# seconds = total_seconds % 60
# print(f"{hours}:{minutes}:{seconds}")