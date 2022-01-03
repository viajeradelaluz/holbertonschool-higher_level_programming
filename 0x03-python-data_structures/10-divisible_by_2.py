#!/usr/bin/python3
def divisible_by_2(my_list=[]):

    result = []
    for num in my_list:
        result.append(False if num % 2 else True)
    return result
