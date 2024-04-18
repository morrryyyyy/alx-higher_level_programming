#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    first = sentence[0]
    for c in sentence:
        if length == 0:
            first = None
        new_tuple = (length, first)
    return new_tuple
