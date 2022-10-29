import random


def split(list_a, chunk_size):
    for i in range(0, len(list_a), chunk_size):
        yield list_a[i: i + chunk_size]


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(split(my_list, 4)))




