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


# Checks if checked percents exceed required pattern percents (Positive or negative)
def check_percents(stock_percents, pattern_object):
    for i in range(len(stock_percents)):
        if stock_percents[i] > 0:  # Increases
            if stock_percents[i] < pattern_object.percents[i]:  # If the increase is less the req by pattern -> false
                return False
        if stock_percents[i] < 0:  # Decreases
            if stock_percents[i] > pattern_object.percents[i]:  # If the decrease is less than req by pattern -> false
                return False
    return True


def pattern_finder(stock_object, pattern_object):
    # Initial values
    stock_data = stock_object.StockHistory
    close_values = stock_object.get_close_values()
    intervals_list = intervals(close_values)[0]
    percent_list = intervals(close_values)[1]

    # Stores index intervals that the specified pattern is present
    pattern_indexes = []
    full_data_list = []

    # Stores the current values of interval and percents as iteration occurs
    current_compare = intervals_list[0:len(pattern_object.pattern)]
    current_percents = percent_list[0:len(pattern_object.percents)]

    # Loops through all values of interval list and checks for any matches on pattern based on interval and percent
    for i in range(len(intervals_list) - len(pattern_object.pattern) - 1):
        if current_compare == pattern_object.pattern and check_percents(current_percents, pattern_object):
            # Adds the index range that pattern is present to a list
            pattern_indexes.append((i, i+len(pattern_object.pattern)))

            # start and end date for pattern
            start_date = str(stock_data.index[i]).split(" ", 1)[0]
            end_date = str(stock_data.index[i + len(pattern_object.pattern)]).split(" ", 1)[0]

            # Prints and stores all data collected from stocks
            print(pattern_object.name + ' found in ' + stock_object.ticker + ': ' + start_date + ' - ' + end_date)
            # Stored in format -> Ticker#Pattern#Start_Date#End_Date
            full_data_list.append(stock_object.ticker + "#" + pattern_object.name + "#" + start_date + "#" + end_date)

        # Iterates to the next object in the list by removing the first value and appending the next value
        del current_compare[0]
        del current_percents[0]
        current_compare.append(intervals_list[i + len(pattern_object.pattern)])
        current_percents.append(percent_list[i + len(pattern_object.percents)])

    # Write collected data to a file
    data_file = open("stock_data.txt", "a")
    for data in full_data_list:
        data_file.write(data + "\n")


# Creates ticker list (S&P 500 tickers)
ticker_list = []
with open("SP500.txt") as f:
    lines = f.readlines()
    for line in lines:
        ticker_list.append(line.strip())


# Patterns
triple_top = Pattern("TripleTop", ['I', 'D', 'I', 'D', 'I', 'D'], [5, -5, 5, -5, 5, -5])
upside_breakout = Pattern("DownsideBreakout", ['D', 'I', 'D', 'I'], [-15, 15, -15, 20])
# Double bottom for presentation

# Iterate through all tickers in list
for ticker in ticker_list:
    stock = StockImporter(ticker)
    pattern_finder(stock, upside_breakout)

# for i in range(20):
# stock = StockImporter(ticker_list[i])
# pattern_finder(stock, triple_top)


