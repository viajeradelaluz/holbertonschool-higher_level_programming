#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = a_dictionary.copy()
    for key in new_dict.keys():
        elm = new_dict.get(key, None) * 2
        new_dict.update({key: elm})

    return new_dict
