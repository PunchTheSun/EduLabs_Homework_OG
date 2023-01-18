## A16-id check digit

# num = input("Enter ID Number: ")
# last_digit = int(num[-1])
# multiplied_num = []
# single_digits = []
# sum_single_digits = 0
# for i in range(len(num)-1,0,-1):
#     if i % 2 == 0:
#         multiplied_num.append(int(num[i-1])*2)
#     else:
#         multiplied_num.append(int(num[i-1]))
# for val in multiplied_num:
#     if val>9:
#         single_digits.append(val//10)
#         single_digits.append(val%10)
#     else:
#         single_digits.append(val)
# for digit in single_digits:
#     sum_single_digits += digit
# print(10-sum_single_digits%10 == last_digit)



## Bonus Exercise:
# import random
# id_num = []
# multiplied_num_GEN = []
# single_digits_GEN = []
# sum_single_digits_GEN = 0
# num_GEN = input("Enter ID Number: ")
# if not num_GEN.isnumeric() and num_GEN != "":
#     print("Invalid input.")
#     exit(1)
# if num_GEN != "":
#     for index in range(0, len(num_GEN)):
#         id_num.append(int(num_GEN[index]))
# if len(num_GEN) < 8:
#     for i in range(len(num_GEN),8):
#         id_num.append(random.randint(0,9))
# else:
#     for j in range(0,9):
#         id_num.append(int(num_GEN[j]))
#
# for multiply_index, multiply_val in enumerate(id_num):
#     if (multiply_index+1) % 2 == 0:
#         multiplied_num_GEN.append(multiply_val*2)
#     else:
#         multiplied_num_GEN.append(multiply_val)
#
# for val in multiplied_num_GEN:
#     if val>9:
#         single_digits_GEN.append(val//10)
#         single_digits_GEN.append(val%10)
#     else:
#         single_digits_GEN.append(val)
#
# for digit in single_digits_GEN:
#     sum_single_digits_GEN += digit
# if sum_single_digits_GEN%10 != 0:
#     id_num.append(10 - sum_single_digits_GEN%10)
# else:
#     id_num.append(0)
# print(id_num)
#
#
# ## Self checking (by using exercise 1 without the bonus), Entering generated ID number as the input
# num = input("Enter ID Number: ")
# last_digit = int(num[-1])
# multiplied_num = []
# single_digits = []
# sum_single_digits = 0
# for i in range(len(num)-1,0,-1):
#     if i % 2 == 0:
#         multiplied_num.append(int(num[i-1])*2)
#     else:
#         multiplied_num.append(int(num[i-1]))
# for val in multiplied_num:
#     if val>9:
#         single_digits.append(val//10)
#         single_digits.append(val%10)
#     else:
#         single_digits.append(val)
# for digit in single_digits:
#     sum_single_digits += digit
# print(10-sum_single_digits%10 == last_digit)