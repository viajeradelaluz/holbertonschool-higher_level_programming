#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    counter = 0
    elm = 0
    while (elm < x):
        try:
            if type(my_list[elm]) is int:
                print("{:d}".format(my_list[elm]), end="")
                counter += 1
        except (TypeError, ValueError):
            pass
        elm += 1
    print("")
    return counter
