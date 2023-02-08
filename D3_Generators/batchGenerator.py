
def batch_generator(n: int, my_list: list):
    counter = 0
    end_counter = len(my_list)//n

    while counter < end_counter:
        batch_list = my_list[n*counter:n*counter+n]
        counter += 1
        yield batch_list

# if __name__ == "__main__":
#     temp_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
#     for batch in batch_generator(3,temp_list):
#         print(batch)
