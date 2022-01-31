#!/usr/bin/python3
""" Square #1

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
