import random


# Splits a list into sub-lists of the specified chunk size
def split(list_a, chunk_size):
    for i in range(0, len(list_a), chunk_size):
        yield list_a[i: i + chunk_size]


increasing_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
decreasing_list = increasing_list[::-1]
random_list = [1, 2, 3, 2, 5, 7, 5, 4, 2, 6]
# print(list(split(increasing_list, 4)))


# Groups list into smaller increasing and decreasing groups
def grouping(list_a):
    # Initial variables
    main = []
    temp_group = []
    is_increasing = True

    # Check first two values to see if list begins by increasing
    if list_a[0] > list_a[1]:
        is_increasing = False

    # Check values in list in pairs
    for current, after in zip(list_a, list_a[1:]):
        temp_group.append(current)

        # Create group and add to main list if the list swaps increasing/decreasing
        if (after < current and is_increasing) or (after > current and not is_increasing):
            main.append(temp_group)
            temp_group = []
            is_increasing = not is_increasing

    print(main)
    return main


# Determines the intervals which the values are increasing and decreasing
def intervals(list_a):
    main = grouping(list_a)
    interval_list = []
    for group in main:
        if not len(group) < 2:
            if group[0] < group[1]:
                interval_list.append("I")
            else:
                interval_list.append("D")
    print(interval_list)


intervals(random_list)

# increasing(decreasing_list, 0, len(decreasing_list))
# increasing(random_list, 0, len(random_list))






