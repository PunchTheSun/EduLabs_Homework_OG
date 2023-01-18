# A15-Easy for loop exercises

# Ex1
# one_prev_num = 1
# two_prev_num = 0
# print("0\n1")
# for r in range(0,8):
#     temp = one_prev_num + two_prev_num
#     print(temp)
#     two_prev_num = one_prev_num
#     one_prev_num = temp

# Ex2
# my_list1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# for r in range(0,len(my_list1)):
#     if r % 2 != 0:
#         print(my_list1[r])

#another option without using range:
# my_list1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# for i, val in enumerate(my_list1):
#     if i % 2 != 0:
#         print(val)

# Ex3
# cities = ['New York', 'Kyiv', 'Paris', 'London', 'Tel Aviv']
# countries = ['USA', 'Ukraine', 'France', 'UK', 'Israel']
# for i, val in enumerate(cities):
#     print(f"{cities[i]}-{countries[i]}")

# Ex4
# num = int(input("Enter a number: "))
# for i, val in enumerate(range(1,num+1)):
#     print(f"The number is: {i+1} and the cube value is: {val**3}")

# Ex5
# num = int(input("Enter a number: "))
# sum = 0
# multiplier = 1
# equation = ""
# for i, val in enumerate(range(1,num+1)):
#     sum += 2*multiplier
#     equation += str(multiplier*2) + " + "
#     multiplier = (multiplier * 10)+1
# equation = list(equation)
# equation[-2] = "="
# equation_string = "".join(equation)
# print(f"{equation_string}{sum}")

# Ex6
# names = ['Moshe', 'Orly', 'David', 'Jack', 'Ofer', 'James']
# doctors = []
# for val in names:
#     doctors.append("Dr."+val)
# print(doctors)

# Ex7
# num = int(input("Enter a number: "))
# squares = []
# for val in range(1,num+1):
#     squares.append(val**2)
# print(squares)

# Ex8 (instead of an example_list you can get values as an input and make that the checked list)
# example_list = ['AAA', [4, 5, 7], "5", 5,  3.0, True, 2654, -4, 0]
# pos_nums = []
# for val in example_list:
#     if type(val) == int:
#         if val > 0:
#             pos_nums.append(val)
# print(pos_nums)

# Ex9
# even_counter = 0
# odd_counter = 0
# numbers = [1,5,8,2,5,9,4,3] #5 ODD numbers, 3 EVEN numbers
# for val in numbers:
#     if val%2==0:
#         even_counter += 1
#     else:
#         odd_counter += 1
# print(f"Even numbers in the list: {even_counter}\nOdd numbers in the list: {odd_counter}")

# Ex10
# my_list = ['AAA', [4, 5, 7], "5", 5,  3.0, True, 2654, -4, 0]
# temp_string = ""
# for val in my_list:
#     temp_string = str(type(val))
#     temp_string = temp_string.replace("<class '","")
#     temp_string = temp_string.replace("'>","")
#     print(f"The value {val} is {temp_string}")

# Ex11
# num = int(input("Enter a number: "))
# for val in range(1,num+1):
#     message = ""
#     if val % 3 == 0 and val % 5 == 0:
#         message = "FizzBuzz"
#     elif val % 3 == 0:
#         message = "Fizz"
#     elif val % 5 == 0:
#         message = "Buzz"
#     if message == "":
#         print(val)
#     else:
#         print(message)

# Ex12
# rows = int(input("Amount of rows: "))
# columns = int(input("Amount of columns: "))
# for val_r in range(1,rows+1):
#     for val_c in range(1,columns+1):
#         print("$",end="")
#     print("")

# Ex13
# n = int(input("Enter a number: "))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(i,end="")
#     print("")