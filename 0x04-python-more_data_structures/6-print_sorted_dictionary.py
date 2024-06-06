#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary={}):
    new_list = list()
    new_list = sorted(a_dictionary.keys())
    for item in new_list:
        value = a_dictionary[item]
        print(f'{item}: {value}')