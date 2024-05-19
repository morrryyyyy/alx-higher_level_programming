#!/usr/bin/python3
import sys
''' This program checks the number of command-line
    arguments and prints them out'''
# make sure script is not run directly
if __name__ == '__main__':
    args = sys.argv
    num_args = (len(args) - 1)

    if num_args == 0:
        print("0 arguments.")
    elif num_args == 1:
        print("1 argument:")
    else:
        print("{0} arguments:".format(num_args))

    for i in range(1, len(args)):
        print("{0}: {1}".format(i, args[i]))
