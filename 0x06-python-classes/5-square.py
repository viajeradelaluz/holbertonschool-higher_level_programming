#!/usr/bin/python3
""" Set the Square class """


class Square:
    """ Defines 'size' as private instance attribute """

    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if isinstance(value, int):
            if value >= 0:
                self.__size = value
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print()

        area_value = self.__size ** 2
        to_print = "#" * self.__size

        counter = 1
        while counter <= area_value:
            if counter <= self.__size:
                print(to_print)
            counter += 1
