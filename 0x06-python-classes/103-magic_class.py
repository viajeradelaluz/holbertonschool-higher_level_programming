#!/usr/bin/python3
""" Raising the power of beating the bytecode. """
import math


class MagicClass:

    """ Define the radius attribute """
    def __init__(self, radius=0):
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    """ Set the power of radius and math.pi """
    def area(self):
        return (self.__radius ** 2) * math.pi

    """ Circum the radius """
    def circumference(self):
        return 2 * math.pi * self.__radius
