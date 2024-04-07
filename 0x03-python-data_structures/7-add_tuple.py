#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # If a tuple is smaller than 2 elements, pad it with zeros
    a = tuple_a + (0, 0) if len(tuple_a) < 2 else tuple_a[:2]
    b = tuple_b + (0, 0) if len(tuple_b) < 2 else tuple_b[:2]

    # Calculate the sum of corresponding elements from both tuples
    result = (a[0] + b[0], a[1] + b[1])

    return result
