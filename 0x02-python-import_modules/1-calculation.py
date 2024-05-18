#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
a = 10
b = 5
sum = add(a, b)
diff = sub(a, b)
prod = mul(a, b)
quo = div(a, b)

print("{0} + {1} = {2}".format(a, b, sum)
print("{0} - {1} = {2}".format(a, b, diff)
print("{0} * {1} = {2}".format(a, b, prod)
print("{0} / {1} = {2}".format(a, b, quo)
