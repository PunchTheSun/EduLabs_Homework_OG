# A13-For loops

# Ex1
# num = int(input("Enter a number: "))
# sum = 0
# for i in range(num+1):
#     sum += i
# print(sum)

# Ex2
# numbers = [-10,-11,13,5,9,200,30,-3]
# minimum = numbers[0]
# for val in numbers:
#     if val<=minimum:
#         minimum = val
# print(minimum)

# Ex3
# my_list = [3,3,3] # Or you can recieve a list as input with a while / for loop
# max_num = -1
# second_max_num = -1
# if len(my_list) < 2:
#     print(f"There is only one number in the list: {my_list[0]}")
# else:
#     for val in my_list:
#         if val > max_num:
#             second_max_num = max_num
#             max_num = val
#         if val > second_max_num and val < max_num:
#             second_max_num = val
# if my_list.count(my_list[0]) == len(my_list):
#     print("There is no 2nd largest number, All the numbers are the same")
# else:
#     print(f"The second largest number is: {second_max_num}")

# Ex4
# numbers = [-10,-11,13,5,9,200,30,-3]
# for val in numbers[::-1]:
#     print(val)

# Ex5
# days = None
# months = None
# years = None
# date = []
# winter = []
# spring = []
# summer = []
# autumn = []
#
# print("Enter 10 dates: ")
# for i in range(0, 10):
#     days, months, years = input().split(".")
#     days = int(days)
#     months = int(months)
#     years = int(years)
#     date.append([days, months, years])
#     if date[i][1] == 12 or date[i][1] == 1 or date[i][1] == 2:
#         winter.append(date[i])
#     elif date[i][1] == 3 or date[i][1] == 4 or date[i][1] == 5:
#         spring.append(date[i])
#     elif date[i][1] == 6 or date[i][1] == 7 or date[i][1] == 8:
#         summer.append(date[i])
#     else:
#         autumn.append(date[i])
#
# print(f"You entered {len(winter)} dates in winter:\n {winter}")
# print(f"You entered {len(summer)} dates in summer:\n {summer}")
# print(f"You entered {len(spring)} dates in spring:\n {spring}")
# print(f"You entered {len(autumn)} dates in autumn:\n {autumn}")

# Ex6
# num = int(input("Enter a number: "))
# factorial = 1
# if num == 0:
#     print(factorial)
# else:
#     for i in range(1,num+1):
#         factorial = factorial*i
# print(factorial)

# Ex7
# num = int(input("Enter a number: "))
# for i in range(1,11):
#     print(f"({i.zfill(2)}) * {num} = {i*num}")

# Ex8
# num = int(input("Enter a number: "))
# for i in range(1, num+1):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print("")

# Ex9
# num = int(input("Enter a number: "))
# prime_nums = [0,1]
# prime = True
# if num > 2:
#     for val in range(3,num+1):
#         for val2 in range(2,num+1):
#             if val % val2 == 0 and val != val2:
#                 prime = False
#         if prime and val not in prime_nums:
#             prime_nums.append(val)
#         prime = True
# print(prime_nums)

# Ex10
# num = int(input("Enter a number: "))
# for i in range(1, num+1):
#     print("* " * i)
# for j in range(num-1, 0, -1):
#     print("* " * j)