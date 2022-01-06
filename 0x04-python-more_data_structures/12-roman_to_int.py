#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or type(roman_string) is not str:
        return 0

    roman_num = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                 'C': 100, 'D': 500, 'M': 1000}

    int_num = []
    for letter in roman_string:
        for symbol in roman_num.keys():
            if letter == symbol:
                int_num.append(roman_num.get(symbol))

    last = len(int_num)
    if last >= 1:
        for i in range(last - 1):
            if int_num[i] < int_num[i + 1]:
                int_num[i] *= -1

    return sum(int_num)
