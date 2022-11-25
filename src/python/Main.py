import random


# Splits a list into sub-lists of the specified chunk size
def split(list_a, chunk_size):
    for i in range(0, len(list_a), chunk_size):
        yield list_a[i: i + chunk_size]


increasing_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
decreasing_list = increasing_list[::-1]
random_list = [1, 2, 3, 2, 5, 7, 5, 4, 2, 6]
# print(list(split(increasing_list, 4)))

###
def increasing(list_a):
    current_value = list_a[0]
    for i in range(len(list_a)):
        if list_a[i] > current_value:
            # Continue loop until not increasing
            current_value = list_a[i]
        elif list_a[i] <= current_value and i > 0 and len(list_a) - len(list_a[i:]) > 1:
            print('stop and warn')
            print('increased from index 0 value ' + str(list_a[0]) + ' to index ' + str(i-1) + ' value ' + str(list_a[i-1]))
            # create list after stop point to end
            print(list_a[i:])
            increasing(list_a[i:])
            break


def increasing_2(list_a):
    current_value = list_a[0]
    for i in range(len(list_a)):
        if i > 0 and list_a[i] < current_value:
            print(list_a[i:])
            increasing_2(list_a[i:])



increasing_2(random_list)
# increasing(decreasing_list, 0, len(decreasing_list))
# increasing(random_list, 0, len(random_list))






