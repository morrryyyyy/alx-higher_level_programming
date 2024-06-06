#!/usr/bin/python3
def number_keys(a_dictionary={}):
    count = 0
    new_list = list(a_dictionary.keys())
    for item in new_list:
        count += 1
    return count
