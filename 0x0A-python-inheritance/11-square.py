#!/usr/bin/python3
""" Square #2

Contains the class Square.
    """


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """ Defines of a square """

    def __init__(self, size):
        """ Builder of the square class """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def __str__(self):
        """ Set the print format """
        to_print = "[Square] {:d}/{:d}".format(self.__size, self.__size)
        return to_print
