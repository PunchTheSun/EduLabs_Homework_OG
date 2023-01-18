## B1 - functions basics

## Ex1
# def sum_list(number_list: list) -> float:
#     sum = 0.0
#     for number in number_list:
#         sum += number
#     return sum

## Main Code - Ex1
# num_list = []
# num = float(input("Enter numbers (enter '-1' to end input): "))
# while num != -1:
#     num_list.append(num)
#     num = float(input("Enter numbers (enter '-1' to end input): "))
# print(sum_list(num_list))


## Ex2
#
# def multiply_tuple(t: tuple) -> float:
#     mult = 1
#     for number in t:
#         mult = mult*number
#     return mult
#
# ## Ex2 - Main Code
# my_tuple = (2,9,10)
# print(multiply_tuple(my_tuple)) # Should return 180


## Ex3
#
# def return_max_of_three(num1: float, num2: float, num3: float) -> float:
#     maximum = max(num1,num2)
#     maximum = max(maximum,num3)
#     return maximum
#
#
# # Ex3 - Main code
# print(return_max_of_three(5.5,30,100.1)) # Should return 100.1


# ## Ex4
#
# def calc_factorial(num: int) -> int:
#     fnumber = 1
#     if num == 0 or num == 1:
#         return fnumber
#     for i in range(2,num+1):
#         fnumber = fnumber*i
#     return fnumber
#
# # Ex4 - Main Code
# num = int(input("Enter a number: "))
# print((calc_factorial(num)))


# Ex5
#
# def unique_tuple(t: tuple) -> tuple:
#     list_unique = []
#     for val in t:
#         if val not in list_unique:
#             list_unique.append(val)
#     return (list_unique[:])
#
# # Ex5 - Main Code
# temp_tuple = (5,5,1,3,4,3,12,1)
# print(unique_tuple(temp_tuple))


## Ex6
#
# def make_unique(l: list[str]) -> list[str]:
#     for i in range(len(l)-1,0,-1):
#         if l.count(l[i]) > 1:
#             l.pop(i)
#     return l
#
# ## Ex6 - Main Code
# temp_list = [5,5,1,3,4,3,12,1]
# temp_list = make_unique((temp_list))
# print(temp_list)


## Ex7
#
# def print_even(l: list) -> None:
#     for val in l:
#         if val % 2 == 0:
#             print(val)
#     return
#
# ## Ex7 - Main Code
# temp_list = [5,5,1,3,4,3,12,1]
# print_even(temp_list)


## Ex8
#
# def isperfect(num: int) -> bool:
#     divisors = []
#     sum_divisors = 0.0
#     for i in range(1,num):
#         if num % i == 0:
#             divisors.append(i)
#     for val in divisors:
#         sum_divisors += val
#     if num == sum_divisors:
#         return True
#     else:
#         return False
#
# # Ex8 - Main Code
# num = int(input("Enter a number: "))
# print(f"Perfect Number: {isperfect(num)}")


# Ex9
# def isprime(num: int) -> bool:
#     prime = True
#     if num == 0 or num == 1:
#         return prime
#     for i in range(2,num):
#         if num % i == 0:
#             prime = False
#     return prime
#
# # Ex9 - Main Code
# num = int(input("Enter a number: "))
# print(isprime(num))


## Ex10
#
# def rev_string(text: str) -> str:
#      return  text[::-1]
#
# ## Ex10 - Main Code
#
# text = input("Enter a string of text: ")
# print(rev_string(text))


## Ex11
#
# def check_range(num: int, rbottom: int, rtop: int) -> bool:
#     if num in range(rbottom,rtop+1):
#         return True
#     return False
#
# ## Ex11 - Main code
# num = int(input("Enter a number: "))
# range_top = int(input("Enter range top number: "))
# range_bottom = int(input("Enter range bottom number: "))
# print(check_range(num,range_bottom,range_top))