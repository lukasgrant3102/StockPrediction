from StockImporter import *
from Pattern import *


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

    return main


# Determines the intervals which the values are increasing and decreasing
def intervals(list_a):
    main = grouping(list_a)
    interval_list = []
    percent_list = []

    for group in main:
        if not len(group) < 2:
            if group[0] < group[1]:
                interval_list.append("I")  # Increase group
            else:
                interval_list.append("D")  # Decrease group
            percent_list.append(round(((group[len(group)-1] - group[0]) / group[0]) * 100))  # (new - old) / old
    return interval_list, percent_list


def check_percents(stock_percents, pattern_object):
    for i in range(len(stock_percents)):
        if stock_percents[i] != pattern_object.percents[i]:
            return False
    return True


def pattern_finder(stock_object, pattern_object):
    # Initial values
    close_values = stock_object.get_close_values()
    intervals_list = intervals(close_values)[0]
    percent_list = intervals(close_values)[1]

    # Stores index intervals that the specified pattern is present
    pattern_indexes = []

    # Stores the current values of interval and percents as iteration occurs
    current_compare = intervals_list[0:len(pattern_object.pattern)]
    current_percents = percent_list[0:len(pattern_object.percents)]

    # Loops through all values of interval list and checks for any matches on pattern based on interval and percent
    for i in range(len(intervals_list) - len(pattern_object.pattern) - 1):
        if current_compare == pattern_object.pattern and check_percents(current_percents, pattern_object):
            pattern_indexes.append((i, i+len(pattern_object.pattern)))
            print('Pattern found in ' + stock_object.ticker + ' at indexes ' + str(i) + '-' + str(i+len(pattern_object.pattern)))

        # Iterates to the next object in the list by removing the first value and appending the next value
        del current_compare[0]
        del current_percents[0]
        current_compare.append(intervals_list[i + len(pattern_object.pattern)])
        current_percents.append(percent_list[i + len(pattern_object.percents)])

    print(pattern_indexes)


# Creates ticker list (S&P 500 tickers)
ticker_list = []
with open("SP500.txt") as f:
    lines = f.readlines()
    for line in lines:
        ticker_list.append(line.strip())


googleStock = StockImporter('GOOG')
triple_top = Pattern(['I', 'D', 'I', 'D', 'I', 'D'], [5, -5, 5, -5, 5, -5])
pattern_finder(googleStock, triple_top)


for ticker in ticker_list:
    stock = StockImporter(ticker)
    pattern_finder(stock, triple_top)

# increasing(decreasing_list, 0, len(decreasing_list))
# increasing(random_list, 0, len(random_list))






