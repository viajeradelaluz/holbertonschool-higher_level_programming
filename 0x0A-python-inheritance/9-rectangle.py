#!/usr/bin/python3
""" Full rectangle

Contains the class Rectangle.
    """

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Defines a rectangle  """

    def __init__(self, width, height):
        """ Builder of the rectangle class """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """ Returns the area of the rectangle """
        return self.__width * self.__height

    def __str__(self):
        """ Set the print format """
        to_print = "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
        return to_print
