#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if my_list:
        if not idx >= len(my_list) or not idx < 0:
            del my_list[idx]

    return my_list
