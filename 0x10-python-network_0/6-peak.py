#!/usr/bin/python3
""" This module solves the following requirements and relies on the file
    test/6-main.py

Write a function that finds a peak in a list of unsorted integers.
    - Prototype: def find_peak(list_of_integers):
    - You are not allowed to import any module
    - Your algorithm must have the lowest complexity (hint: you don't need to go
      through all numbers to find a peak)
    - 6-peak.py must contain the function
    - 6-peak.txt must contain the complexity of your algorithm: O(log(n)), O(n),
      O(nlog(n)) or O(n2)
    - Note: there may be more than one peak in the list
"""


def find_peak(list_of_integers):
    """ Find a peak without going to all numbers """
    if len(list_of_integers) == 0:
        return None

    peak, temp, i = 0, 0, 1

    while i < len(list_of_integers):
        left = list_of_integers[i - 1]
        right = list_of_integers[i]
        temp = left if left > right else right
        peak = temp if temp > peak else peak
        i *= 2
    return peak
