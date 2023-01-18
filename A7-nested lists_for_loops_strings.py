# A7-nested lists, for loops, strings

goods = [['apple', 'pear', 'peach', 'chery' ],
['salak', 'mangustin', 'mango', 'durian', 'breadfruit',
    'bayberry', 'blueberry', 'cloudberry' , 'raspberry', 'blackberry' ]]

# Ex1
# max_length_index = []
# max_length_words = []
# vowel_count = []
# temp_max_length = 0
# vowel_temp = 0
# temp_max_i = None
# temp_max_j = None
# for i, vali in enumerate(goods):
#     for j in range(len(goods[i])):
#         if len(goods[i][j]) > temp_max_length:
#             temp_max_length = len(goods[i][j])
#             temp_max_i = i
#             temp_max_j = j
#     for z in range(len(goods[i])):
#         if len(goods[i][z]) == temp_max_length:
#             max_length_index.append([i, z])
#             max_length_words.append(goods[i][z])
#             vowel_temp += goods[i][z].count("a") + goods[i][z].count("e") + goods[i][z].count("i") + goods[i][z].count("o") + goods[i][z].count("u") + goods[i][z].count("y")
#             vowel_count.append(vowel_temp)
#             vowel_temp = 0
#     temp_max_length = 0
#     temp_max_i = -1
#     temp_max_j = -1
# print(f"Longest words are at the following indexes: \n{max_length_index}")
# print(max_length_words)
# print(f"The Vowel count for each word: \n {vowel_count}")

# Ex2
# index_list = []
# for i, vali in enumerate(goods):
#      for j in range(len(goods[i])):
#          if goods[i][j].startswith("a") or goods[i][j].startswith("e") or goods[i][j].startswith("i") or goods[i][j].startswith("o") or goods[i][j].startswith("u") or goods[i][j].startswith("y"):
#              index_list.append([i,j])
# print(index_list)

# Ex3
# words_with_b = []
# for index in range(len(goods)):
#     for val in goods[index]:
#         if val.__contains__("b") or val.__contains__("B"):
#             words_with_b.append(val)
# print(words_with_b)

# Ex4
# vowel_temp = 0
# sublist_vowels = []
# for i, val_i in enumerate(goods):
#     for z in range(len(goods[i])):
#         vowel_temp += goods[i][z].count("a") + goods[i][z].count("e") + goods[i][z].count("i") + goods[i][z].count("o") + goods[i][z].count("u") + goods[i][z].count("y")
#     sublist_vowels.append(vowel_temp)
#     vowel_temp = 0
# for vowels in sublist_vowels:
#     if vowels > vowel_temp:
#         vowel_temp = vowels
# for j, val_j in enumerate(sublist_vowels):
#     if val_j == vowel_temp:
#         print(f"Sublist indexes with most vowels are:\n{j}")

# Ex 5
# shortest_len = 1000000
# shortest_words = []
# shortest_words_index = []
# for i, val_i in enumerate(goods):
#     for j, val_j in enumerate(goods[i]):
#         if len(val_j) < shortest_len:
#             shortest_len = len(val_j)
# for min_i, fruit_list in enumerate(goods):
#     for min_j, fruit in enumerate(fruit_list):
#         if len(fruit) == shortest_len:
#             shortest_words.append(fruit)
#             shortest_words_index.append([min_i, min_j])
# print(f"Shortest words are:\n{shortest_words}\n Indexes are accordingly:\n{shortest_words_index}")

# Ex6
# berry_word_counter = 0
# berry_word_index = []
# for i, val_i in enumerate(goods):
#     for j, val_j in enumerate(goods[i]):
#         if "berry" in val_j:
#             berry_word_counter += 1
#             berry_word_index.append([i, j])
# print(f'There are {berry_word_counter} words with the word "Berry"\nTheir indexes are accordingly:\n{berry_word_index}')

# Ex7
# for j, fruit_list in enumerate(goods):
#     for i in range(1,len(fruit_list)+1,2):
#         goods[j][i] = goods[j][i]+"2"
# print(goods)

# Ex8
# rev_fruits = []
# for i, val_i in enumerate(goods):
#     for j, val_j in enumerate(goods[i]):
#         if val_j.__contains__("p"):
#             rev_fruits.append((val_j[::-1]))
# print(rev_fruits)

# Ex9
# for fruit_list in goods:
#     for fruit in fruit_list:
#         if len(fruit) > 5:
#             print(fruit)

# Ex10
# total_letters = 0
# single_list = []
# for fruit_list in goods:
#     for fruit in fruit_list:
#         single_list.append(fruit)
#         total_letters += len(fruit)
# print(f"{single_list}\nTotal letters = {total_letters}")

# Ex11
# new_goods = []
# for fruit_list in goods:
#     for fruit in fruit_list:
#         new_goods.append(fruit[0:3])
# print(new_goods)

# Ex12
# single_list = []
# temp_word_start = None
# temp_word_end = None
# for fruit_list in goods:
#     for fruit in fruit_list:
#         single_list.append(fruit)
# for i, fruit in enumerate(single_list):
#    temp_word_start = fruit[0:len(fruit)-3]
#    temp_word_end = fruit[-1:-4:-1]
#    single_list[i] = temp_word_end+temp_word_start
# print(single_list)