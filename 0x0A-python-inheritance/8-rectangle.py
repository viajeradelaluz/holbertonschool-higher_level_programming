#!/usr/bin/python3
""" Rectangle

Contains the class Rectangle.
    """

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Define a rectangle  """

    def __init__(self, width, height):
        """ Builder of the rectangle class """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
