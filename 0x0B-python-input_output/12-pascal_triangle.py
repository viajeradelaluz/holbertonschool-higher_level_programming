#!/usr/bin/python3
"""Pascal's Triangle
    """


def pascal_triangle(n):
    """ Returns a pascal triangle"""

    list = []

    for n in range(n):
        list.append([])
        list[n].append(1)
        for m in range(1, n):
            list[n].append(list[n - 1][m - 1] + list[n - 1][m])
        if(n != 0):
            list[n].append(1)

    return list
