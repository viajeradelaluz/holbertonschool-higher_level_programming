#!/usr/bin/python3
""" Set the Square class """


class Square:
    """ Defines 'size' as private instance attribute """

    def __init__(self, size=0):
        try:
            if size >= 0:
                self.__size: int = size
            else:
                raise ValueError("size must be >= 0")
        except TypeError:
            raise TypeError("size must be an integer")
