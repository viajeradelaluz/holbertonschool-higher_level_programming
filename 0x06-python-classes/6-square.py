#!/usr/bin/python3
""" Set the Square class """


class Square:
    """ Defines 'size' as private instance attribute """

    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if isinstance(value, tuple) or len(value) == 2 or\
                isinstance(value[0], int) or isinstance(value[1], int) or\
                value[0] < 0 or value[1] < 0:
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print()

        area_value = self.__size ** 2
        print_size = "#" * self.__size

        counter = 1
        while counter <= area_value:
            if counter <= self.__size:
                print("{}{}".format(" " * self.position[0], print_size))
            counter += 1
