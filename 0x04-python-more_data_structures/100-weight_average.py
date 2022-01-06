#!/usr/bin/python3
def weight_average(my_list=[]):
    score = 0
    weight = 0
    for tuple in my_list:
        a, b = tuple
        score += a * b
        weight += b

    return score / weight
