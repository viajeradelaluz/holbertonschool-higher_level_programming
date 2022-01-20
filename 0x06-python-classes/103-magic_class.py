#!/usr/bin/python3
import math


class MagicClass:
    """ Raising the power of beating the bytecode """

    def __init__(self, radius=0):
        """ Define the radius attribute """
        self.radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """ Set the power of radius and math.pi """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """ Circum the radius """
        return 2 * math.pi * self.__radius
