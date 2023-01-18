## B3 - functions level 2

# Ex1
#
# def reverse_hyphen(text: str) -> str:
#     rev_text = ""
#     sep_text = text.split("-")
#     sep_text = sorted(sep_text)
#     for val in sep_text:
#         rev_text += val+"-"
#     rev_text = rev_text[0:len(rev_text)-1]
#     return  rev_text
#
# # Ex1 - Main code
# text = input("Enter a string of text seperated by '-': \n")
# print(reverse_hyphen(text))


# Ex2
#
# def is_correct_input(a: int, b: int, c: int) -> bool:
#     if a>0 and b>0 and c>0:
#         return True
#     else:
#         return False
#
# def is_triangle(a: int, b: int, c: int) -> bool:
#     if a+b > c and b+c > a and c+a > b:
#         return True
#     else:
#         return False
#
# def get_triangle_area(a: int, b: int, c: int) -> float:
#     s = (a+b+c)/2
#     area = (s*(s-a)*(s-b)*(s-c))**0.5
#     return area
#
# def get_triangle_perimeter(a: int, b: int, c: int) -> int:
#     return a+b+c
#
# # Ex2 - Main Code
#
# a = int(input("Enter triangle 1st side: "))
# b = int(input("Enter triangle 2nd side: "))
# c = int(input("Enter triangle 3rd side: "))
#
# if is_correct_input(a,b,c):
#     if is_triangle(a,b,c):
#         print(f"Triangle area: {get_triangle_area(a,b,c)}")
#         print(f"Triangle perimeter: {get_triangle_perimeter(a,b,c)}")
#     else:
#         print("Not a triangle.")
# else:
#     print("Invalid input.")


# # Ex3
# stored_words = []
#
# def insert(word: str) -> None:
#     stored_words.append(word)
#     return
#
# def search(letter: str, num: int) -> None:
#     for val in stored_words:
#         if val.count(letter) == num:
#             print(val)
#         else:
#             print("No matches found")
#     return
#
# # Ex3 - Main Code
# while True:
#     choice = input("Input '1' to insert or '2' to search (insert '-' to exit): ")
#     match choice:
#         case '1':
#             insert(input("Insert a word: "))
#         case '2':
#             search(input("Insert a letter: "),int(input("Insert a number: ")))
#         case '-':
#             exit(0)
#         case _:
#             print("Invalid input, please try again")


# Ex4
#
# def count_lower_upper(text: str) -> tuple:
#     upper_count = 0
#     lower_count = 0
#     for i in range(0,len(text)):
#         if text[i].isupper():
#             upper_count += 1
#         elif text[i].islower():
#             lower_count += 1
#     return (upper_count,lower_count)
#
# # Ex4 - Main Code
#
# text = input("Enter a string of text: ")
# print(f"Amount of uppercase letters and lowercase letters\n(Uppercase, Lowercase)\n{count_lower_upper(text)}")


# Ex5

# def is_pangram(text: str) -> bool:
#     compare_set = set(" ")
#     letters = {"a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"}
#     letters_cap = {"A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"}
#     unique_text = set(text.lower())
#     compare_set = compare_set.union(unique_text.intersection(letters))
#     compare_set = compare_set.union(unique_text.intersection(letters_cap))
#     compare_set.remove(" ")
#     if len(compare_set) == 26:
#         return True
#     return False
#
# # Ex5 - Main Code
#
# text = input("Enter a string of text: ")
# result = False
# result = is_pangram(text)
# print(f"Is a pangram: {result}")


# Ex6

# def is_palindrome(text: str) -> bool:
#     return text == text[::-1]
#
# text = input("Enter a string of text: ")
# print(f"Palindrome text: {is_palindrome(text)}")


# Ex7
#
# def calc_squares() -> None:
#     for i in range(1,31):
#         print(f"{i**2}")
#     return
#
# Ex7 Main Code
# calc_squares()


# Ex8
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


# Ex9 - Can't quite get the formatting with the correct padding formula, did my best here :)

# def pascal_triangle(n: int) -> None:
#     curr_line = [1]
#     prev_line = []
#     for line in range(0,n):
#         print(" "*(n-line), end="")
#         for digit in curr_line:
#             print(f"{digit}", end=" ")
#         print(" " * (n - line))
#         prev_line = curr_line
#         curr_line = [1]
#         for i in range(1,line+1):
#             curr_line.append(prev_line[i-1]+prev_line[i])
#         curr_line.append(1)
#     return
#
# # Ex9 Main Code
# num = int(input("Enter a number of lines: "))
# pascal_triangle(num)


# Ex10

# def text_to_code(text: str) -> None:
#     exec(text)
#     return
#
# # Ex10 Main Code
# line_of_code = input("Enter a line of code in python: ")
# text_to_code(line_of_code)