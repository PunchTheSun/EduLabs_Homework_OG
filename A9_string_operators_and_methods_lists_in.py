# A9-string operators and methods, lists, in

# Ex1
# word = input("Enter a word (No numbers or spaces): ")
# if word.isalpha():
#     print(f"The word is {len(word)} letters long.")
# else:
#     print("Invalid input, Not a word.")


# Ex2
# word = input("Enter a word (No numbers or spaces): ")
# if word.isalpha():
#     if word == word[::-1]:
#         print("Palindrom.")
#     else:
#         print("Not Palindrom.")
# else:
#     print("Invalid input, Not a word.")

# Ex3
# word = input("Enter a string of text: ")
# if len(word) > 0 and not word.isspace():
#     word = word.strip() # I was trying to handle whitespaces at the start and finish of the string, figured they should not count as chars or I need to find a better way of counting words.
#     print(f"Amount of words: {word.count(' ')+1}")
#     print(f"Amount of chars: {len(word)}")
#     print(f"Amount of non-whitespace chars: {len(word)-word.count(' ')}")
#     print(f"Amount of vowels (a, e, i, o, u): "
#           f"{word.count('a')+word.count('e')+word.count('i')+word.count('o')+word.count('u')+word.count('y')+word.count('A')+word.count('E')+word.count('I')+word.count('O')+word.count('U')+word.count('Y')}")
# else:
#     print("Invalid input, Not a string of text.")

# Ex4
# word = input("Enter a word: ")
# if word.endswith('a') or word.endswith('e') or word.endswith('i') or word.endswith('o') or word.endswith('u') or word.endswith('y')):
#     print(f"The word {word} ends with the vowel {word[len(word)-1]}.")
# else:
#     print(f"The word {word} doesn't end with a vowel.")
# word = input("Enter a string of text: ")
# is_whitespaces = ""
# if not word.isspace():
#     is_whitespaces = "not "
# print(f"This string of text is {is_whitespaces}only whitespaces.")
# word = input("Enter a sentence: ")
# print(f"{word.title()}")

# Ex5
# layout1 = input("Enter seat layout (1st batch) in letters seperated by spaces (A, AB, ABC):  ")
# if not layout1.isspace():
#     layout_list = layout1.split(" ")
#     if len(layout_list) > 0:
#         print(f"{len(layout_list[0])}", end=" ")
#         if len(layout_list) > 1:
#             print(f"{len(layout_list[1])}", end=" ")
#             if len(layout_list) > 2:
#                 print(f"{len(layout_list[2])}")
# else:
#     print("Invalid input.")

# Ex6
# layout_unsplit = input("Enter seat layout in separated by spaces (A, AB, ABC):  ")
# layout = layout_unsplit.split(" ")
# seat_index = input("Enter seat index: ")
# if len(seat_index) > 2:
#     print(f"Row number: {seat_index[0:2]}")
# else:
#     print(f"Row number: {seat_index[0]}")
# seat = seat_index[len(seat_index)-1]
# print(f"Chair Index: {seat}")
#
# seat_type = ""
# if seat == layout[0][0] or seat == layout[-1][-1]:
#     seat_type = "Window"
# if seat_type != "Window":
#     if len(layout) == 1:
#         seat_type = "Middle"
#     if len(layout) == 2:
#         if seat == layout[0][-1] or seat == layout[1][0]:
#             seat_type = "Aisle"
#         else:
#             seat_type = "Middle"
#     if len(layout) == 3:
#         if seat == layout[0][-1] or seat == layout[1][0] or seat == layout[1][-1] or seat == layout[2][0]:
#             seat_type = "Aisle"
#         else:
#             seat_type = "Middle"
# if layout_unsplit.count(seat) > 0:
#     print(f"Seat type: {seat_type}")
# else:
#     print(f"I'm sorry, {seat} is not a valid chair index on this plane.")