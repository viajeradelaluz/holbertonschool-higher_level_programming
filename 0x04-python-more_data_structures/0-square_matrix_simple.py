#!/usr/bin/python3
def square_matrix_simple(matrix=[]):

    pow = []
    for row in matrix:
        pow.append([i**2 for i in row])

    return pow
