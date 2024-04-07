#!/usr/bin/python3
def multiple_returns(sentence):
    for c in sentence:
        len = len(sentence)
        first = sentence[0]
        if len == 0:
            first = None
        new_tuple = (len, first)
    return new_tuple
