#!/usr/bin/python3
def search_replace(my_list, search, replace):

    new_list = []
    for elm in my_list:
        new_list.append(elm if elm != search else replace)

    return new_list
