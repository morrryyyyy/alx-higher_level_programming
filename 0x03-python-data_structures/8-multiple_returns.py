#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    first = sentence[0] if length > 0 else None
    new_tuple = (length, first)
    return new_tuple
