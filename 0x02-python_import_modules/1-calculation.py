#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
a = 10
b = 5
sum = add(a, b)
diff = sub(a, b)
prod = mul(a, b)
quo = div(a, b)

print(f"{a} + {b} = {sum}")
print(f"{a} - {b} = {diff}")
print(f"{a} * {b} = {prod}")
print(f"{a} / {b} = {quo}")
