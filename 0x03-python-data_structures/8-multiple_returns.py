#!/usr/bin/python3
def multiple_returns(sentence):

    len_sen = len(sentence)
    new_tuple = (len_sen, sentence[0] if sentence != "" else None)

    return new_tuple
