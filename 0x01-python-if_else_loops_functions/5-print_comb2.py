#!/usr/bin/python3
for i in range(0, 100):
    tens = i // 10
    unit = i % 10
    if tens != 9 or unit != 9:
        print("{}{}".format(tens, unit), end=', ')
    if tens == 9 and unit == 9:
        print("{}{}".format(tens, unit))
        print("")
