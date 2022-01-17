#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    counter = 0
    for elm in my_list:
        try:
            if elm <= x:
                print("{:d}".format(elm), end="")
                counter += 1
        except IndexError:
            break
    print("")
    return counter
