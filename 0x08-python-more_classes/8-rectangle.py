#!/usr/bin/python3
""" Rectangle

Define the class Rectangle
    """


class Rectangle:
    """ Representation of a rectangle """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ Initialize the rectangle """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
        st = ""
        if self.__width != 0 and self.__height != 0:
            st = (str(self.print_symbol) * self.__width + "\n") * self.__height
            st = st[:-1]
        return st

    def __repr__(self):
        """ Extract the representation of the rectangle with repr """
        rep = "Rectangle({self.width}, {self.height})".format(self=self)
        return rep

    def __del__(self):
        """ Set message for __del__ destructor """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ [summary] """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2
