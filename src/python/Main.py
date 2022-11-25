import random


# Splits a list into sub-lists of the specified chunk size
def split(list_a, chunk_size):
    for i in range(0, len(list_a), chunk_size):
        yield list_a[i: i + chunk_size]


increasing_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
decreasing_list = increasing_list[::-1]
random_list = [1, 2, 3, 2, 5, 7, 5, 4, 2]
print(list(split(increasing_list, 4)))


def increasing(list_a, start, length):
    start_index = start
    original_length = length

    for i in range(len(list_a)):
        if i > 0:
            if list_a[i] < list_a[i-1]:
                print('List increases from index: ' + str(start_index) + ", to index: " + str((start_index + i)-1))
                increasing(list_a[i: len(list_a)], i+start_index, original_length)
                break

            if i == len(list_a) - 1:
                print('List increases from index: ' + str(start_index) + ", to index: " + str(original_length-1))


# increasing(increasing_list, 0, len(increasing_list))
increasing(decreasing_list, 0, len(decreasing_list))
# increasing(random_list, 0, len(random_list))






