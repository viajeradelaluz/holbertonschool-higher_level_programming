#!/usr/bin/python3
""" Rectangle

Define the class Rectangle
    """


class Rectangle:
    """ Representation of a rectangle """

    def __init__(self, width=0, height=0):
        """ Initialize the rectangle """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Method that returns the width of the retangle """
        return self.__width

    @width.setter
    def width(self, value):
        """ Method that sets the width of the rectangle """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Method that returns the height of the retangle """
        return self.__height

    @height.setter
    def height(self, value):
        """ Method that sets the height of the rectangle """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Method to calculate the rectangle area """
        return self.__width * self.__height

    def perimeter(self):
        """ Method to calculate the rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """ Method to represent the rectangle with # """

        to_print = ""
        if self.__width != 0 and self.__height != 0:
            to_print = ("#" * self.__width + "\n") * self.__height
            to_print = to_print[:-1]

        return to_print
