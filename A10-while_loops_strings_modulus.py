# A10-while loops, strings, modulus

# Ex1
# num = int(input("Enter a number: "))
# count = 0
# while count <= num:
#     print(count)
#     count += 1

# Ex2
# num = int(input("Enter a number: "))
# count = 1
# while count <= num:
#     print(count)
#     count += 3

# Ex3
# sum = 0
# count = 0
# num = " "
# while num != "$$$":
#     num = input("Enter a number: ")
#     if num.isnumeric():
#         sum += int(num)
#         count += 1
# print(f"The sum is: {sum} and the average is: {sum/count}")

# Ex4
# sum = 0
# count = 0
# students = []
# while True:
#     temp_var = input("Enter a student's First Name: ")
#     if temp_var == "$$$":
#         break
#     elif temp_var.isalpha():
#         students.append(temp_var)
#         temp_var = input(f"Enter {students[count]}'s grade: ")
#         if temp_var.isnumeric():
#             sum += int(temp_var)
#             count += 1
#         else:
#             print("Invalid input, not a number.\nRemoving student from database, please Re-Enter.")
#             students.pop()
#     else:
#         print("Invalid input, Not a name.\nRemoving student from database, please Re-Enter.")
# print(f"Students names:\n{students}\nAverage grade: {sum//count}")

# Ex5
# num_strings = 0
# num_characters = 0
# num_digits = 0
# while True:
#     temp_val = input("Enter a string: ")
#     if temp_val == "$":
#         break
#     num_strings += 1
#     num_characters += len(temp_val)
#     if temp_val.isnumeric():
#         num_digits += len(temp_val)
# print(f"Number of strings recieved: {num_strings}\nNumber of characters recieved: {num_characters}\nNumber of digits recieved: {num_digits}")

# Ex6
# text = []
# matches_counter = 0
# while True:
#     text.append(input("Enter a string: "))
#     if len(text[-1]) % 2 == 0:
#         matches_counter += 1
#     if len(text) >= 10:
#         break
# print(f"Amount of strings with EVEN length: {matches_counter}")

# Ex7
# num = 100
# while True:
#     num = int(input("Enter a number: "))
#     if num % 2 != 0:
#         break

# Ex8
# num_digits = 0
# num = int(input("Enter a number: "))
# while True:
#     num_digits += 1
#     if num < 10:
#         break
#     num = num/10
# print(f"The amount of digits: {num_digits}")

# Ex9
# # Option a: recieve num as string
# num = input("Enter a number: ")
# new_num = ""
# count = len(num)-1
# while count >= 0:
#     new_num += num[count]
#     count -= 1
# print(new_num)
#
# # Option b: recieve num as int
# num = int(input("Enter a number: "))
# rev_num = 0
# while num != 0:
#     rev_num = rev_num * 10
#     rev_num += num % 10
#     num = num // 10
# print(rev_num)

# Ex10
# wins_p1 = 0
# wins_p2 = 0
# draws = 0
# rounds_played = 0
# while True:
#     rounds_played += 1
#     player1 = input("Enter 1st player's play (R / P / S): ")
#     player2 = input("Enter 2nd player's play (R / P / S): ")
#     if player1 == 'R':
#         if player2 == 'R':
#             print("TIE GAME")
#             draws += 1
#         elif player2 == 'P':
#             print("Player 2 WINS")
#             wins_p2 += 1
#         elif player2 == 'S':
#             print("Player 1 WINS")
#             wins_p1 += 1
#
#     if player1 == 'S':
#         if player2 == 'S':
#             print("TIE GAME")
#             draws += 1
#         elif player2 == 'R':
#             print("Player 2 WINS")
#             wins_p2 += 1
#         elif player2 == 'P':
#             print("Player 1 WINS")
#             wins_p1 += 1
#
#     if player1 == 'P':
#         if player2 == 'P':
#             print("TIE GAME")
#             draws += 1
#         elif player2 == 'S':
#             print("Player 2 WINS")
#             wins_p2 += 1
#         elif player2 == 'R':
#             print("Player 1 WINS")
#             wins_p1 += 1
#     rematch = input("Would you like to play again (Y/N): ")
#     if rematch == "N":
#         break
# print(f"Game statistics:\nRounds played: {rounds_played}\nTie games: {draws}\nPlayer 1 Wins: {wins_p1}\nPlayer 2 Wins: {wins_p2}")

# Ex11
# import random
# rnum = random.randint(1,100)
# guess = None
# guess_counter = 0
# while guess != rnum:
#     guess = input("Guess a number between 1-100: ")
#     if guess == "exit":
#         break
#     guess = int(guess)
#     guess_counter += 1
#     if guess > rnum:
#         print("Too high, guess again")
#     elif guess < rnum:
#         print("Too low, guess again")
#     else:
#         print("BULLSEYE! Well done.")
# print(f"Amount of guesses: {guess_counter}")


