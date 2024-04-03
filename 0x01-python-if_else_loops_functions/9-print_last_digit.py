#!/usr/bin/python3
def print_last_digit(number):
    abs_number = abs(number)
    last = abs_number % 10
    print("{}".format(last), end = '')
    return last
