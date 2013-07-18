#!/usr/bin/env python
'''
Extract Number

Input: A list of dictionaries with text that includes time
Output: Strip the tmie out of the text, convert to time, calculate the average time and return the mean.

Challenge: Account for military time. Account for
'''
import re  # import regex

# Strip out time with Regex


def strip_time(string):
    str_time = re.search('\d+:\d+', string)
    if str_time:  # if it exists then return
        time_list = str_time.group().split(':')
        return time_list

# Convert time to int and calc mean


def get_mean(time_list):
    hours = minutes = 0
    for time in time_list:
        if time:
            hours += int(time[0])
            minutes += int(time[1])

    list_len = len(time_list)
    mean_hour = hours / list_len
    mean_min = minutes / list_len

    print 5, '%d:%d' % (mean_hour, mean_min)

    return '%d:%d' % (mean_hour, mean_min)

# Extract strings from list of dicts and conver to mean time


def dict_mean_time(list_dicts):
    time_list = []
    for dictionary in list_dicts:  # loop list
        for num, string in dictionary.items():  # loop dict
            if strip_time(string):  # confirm time exists
                time_list.append(strip_time(string))  # capture time list

    return get_mean(time_list)

if __name__ == '__main__':
    # Test section
    list_dicts = [{1: "hello at 9:30"}, {
        2: "night at 10:30", 3: "moon at 8:00"}, {0: "no"}]
    implementations = [dict_mean_time]

    for impl in implementations:
        print "trying %s" % impl
        print "  f(list_dicts) == '9:20': %s" % (impl(list_dicts) == '9:20')
