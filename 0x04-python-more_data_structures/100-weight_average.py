#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    score = 0
    weight = 0
    for tuple in my_list:
        a, b = tuple
        score += a * b
        weight += b

    return score / weight
