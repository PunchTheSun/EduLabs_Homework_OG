# A3-Comparison, logical operators, and, or, bool, if else

# Ex1
# num = int(input("Enter a number: "))
# if   num % 2 == 0:
#     print("EVEN NUMBER")
# else:
#     print("ODD NUMBER")

# Ex2
# num = int(input("Enter a number: "))
# if num // 1000 != 0:
#     thousand_mark = True
# else:
#     thousand_mark = False
# if num // 100 != 0:
#     hundreads_mark = True
# else:
#     hundreads_mark = False
# if num // 10 != 0:
#     tens_mark = True
# else:
#     tens_mark = False
# if num // 1 != 0:
#    ones_mark = True
# else:
#     ones_mark = False
#
# amount_of_digits = thousand_mark + hundreads_mark + tens_mark + ones_mark
# print(f"There are {amount_of_digits} digits in this number.")

# Ex3
# num1 = int(input("Enter the 1st number: "))
# num2 = int(input("Enter the 2nd number: "))
# num3 = int(input("Enter the 3rd number: "))
#
# if num1 > num2 and num1 > num3:
#     first_num = num1
#     if num2 > num3:
#         second_num = num2
#         third_num = num3
#     else:
#         second_num = num3
#         third_num = num2
#
# if num2 > num1 and num2 > num3:
#     first_num = num2
#     if num1 > num3:
#         second_num = num1
#         third_num = num3
#     else:
#         second_num = num3
#         third_num = num1
#
# if num3 > num2 and num3 > num1:
#     first_num = num3
#     if num2 > num1:
#         second_num = num2
#         third_num = num1
#     else:
#         second_num = num1
#         third_num = num2
#
# print(f"{first_num} > {second_num} > {third_num}")
# I accidently did it from biggest to smallest and not the other way around, But I understood the idea behind it.

# Ex4
# age = int(input("Enter your age: "))
# height = int(input("Enter your height (cm): "))
#
# if(age >= 8 and age <= 18 and height > 115):
#     print("You can ride.")
# elif (age > 18 and height > 100):
#     print("You can ride.")
# else:
#     print("You can't ride.")

# Ex5
# player1 = input("Enter 1st player's play (R / P / S): ")
# player2 = input("Enter 2nd player's play (R / P / S): ")
# if player1 == 'R':
#     if player2 == 'R':
#         print("TIE GAME")
#     elif player2 == 'P':
#         print("Player 2 WINS")
#     elif player2 == 'S':
#         print("Player 1 WINS")
#
# if player1 == 'S':
#     if player2 == 'S':
#         print("TIE GAME")
#     elif player2 == 'R':
#         print("Player 2 WINS")
#     elif player2 == 'P':
#         print("Player 1 WINS")
#
# if player1 == 'P':
#     if player2 == 'P':
#         print("TIE GAME")
#     elif player2 == 'S':
#         print("Player 2 WINS")
#     elif player2 == 'R':
#         print("Player 1 WINS")

# Ex6
# Spring – starts March 20, 2022
# Summer – starts June 21, 2022
# Fall – starts September 22, 2022
# Winter – starts December 21, 2022
#
# day = int(input("Enter Day: "))
# month = int(input("Enter Month: "))
# year = int(input("Enter Year: "))
#
# if month >= 3 and month < 6:
#     season = "Spring"
# elif month >= 6 and month < 9:
#     season = "Summer"
# elif month >= 9 and month < 12:
#     season = "Fall"
# elif month >= 1 and month < 3:
#     season = "Winter"
#
# if month == 3 and day < 20:
#     season = "Winter"
# elif month == 3 and day >= 20:
#     season = "Spring"
#
# if month == 6 and day < 21:
#     season = "Spring"
# elif month == 6 and day >= 21:
#     season = "Summer"
#
# if month == 9 and day < 22:
#     season = "Summer"
# elif month == 9 and day >= 22:
#     season = "Fall"
#
# if month == 12 and day < 21:
#     season = "Fall"
# elif month == 12 and day >= 21:
#     season = "Winter"
#
# if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
#     days_in_month = 31
# elif month == 4 or month == 6 or month == 9 or month == 11:
#     days_in_month = 30
# else:
#     days_in_month = "28 (or 29 every 4 years)"
#
# print(f"The season is {season} and this month has {days_in_month} days.")

# Ex7
# year = int(input("Enter year: "))
# if year % 100 == 0:
#     if year % 400 == 0:
#         is_leap_year = True
#     else:
#         is_leap_year = False
# elif year % 4 == 0:
#     is_leap_year = True
# else:
#     is_leap_year = False
#
# if is_leap_year:
#     print("It IS a leap year.")
# else: print("it ISN'T a leap year.")

# Ex8
# Spring – starts March 20, 2022
# Summer – starts June 21, 2022
# Fall – starts September 22, 2022
# Winter – starts December 21, 2022

# day = int(input("Enter Day: "))
# month = int(input("Enter Month: "))
# year = int(input("Enter Year: "))
#
# # Leap year calculation from Ex7
# if year % 100 == 0:
#     if year % 400 == 0:
#         is_leap_year = True
#     else:
#         is_leap_year = False
# elif year % 4 == 0:
#     is_leap_year = True
# else:
#     is_leap_year = False
#
# if month >= 3 and month < 6:
#     season = "Spring"
# elif month >= 6 and month < 9:
#     season = "Summer"
# elif month >= 9 and month < 12:
#     season = "Fall"
# elif month >= 1 and month < 3:
#     season = "Winter"
#
# if month == 3 and day < 20:
#     season = "Winter"
# elif month == 3 and day >= 20:
#     season = "Spring"
#
# if month == 6 and day < 21:
#     season = "Spring"
# elif month == 6 and day >= 21:
#     season = "Summer"
#
# if month == 9 and day < 22:
#     season = "Summer"
# elif month == 9 and day >= 22:
#     season = "Fall"
#
# if month == 12 and day < 21:
#     season = "Fall"
# elif month == 12 and day >= 21:
#     season = "Winter"
#
# if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
#     days_in_month = 31
# elif month == 4 or month == 6 or month == 9 or month == 11:
#     days_in_month = 30
# else:
#     if is_leap_year:
#         days_in_month = 29
#     else:
#         days_in_month = 28
#
# print(f"The season is {season} and this month has {days_in_month} days.")
# if is_leap_year:
#     print("It is also a leap year!")