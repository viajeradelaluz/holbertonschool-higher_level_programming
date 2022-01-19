#!/usr/bin/python3
""" Set the Square class """


class Square:
    """ Defines 'size' as private instance attribute """

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

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
        if isinstance(value, tuple) and len(value) == 2 and\
                isinstance(value[0], int) and isinstance(value[1], int) and\
                value[0] >= 0 and value[1] >= 0:
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print()
            return

        area_value = self.__size ** 2
        print_size = "#" * self.__size

        if self.__position[1] > 0:
            print("{}".format("\n" * self.__position[1]), end="")

        counter = 1
        while counter <= area_value:
            if counter <= self.__size:
                print("{}{}".format(" " * self.__position[0], print_size))
            counter += 1
