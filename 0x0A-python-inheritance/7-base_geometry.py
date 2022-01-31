#!/usr/bin/python3
""" Geometry Integer validator

Contains the class BaseGeometry.
    """


class BaseGeometry():
    """ Define public attribute area and integer validator  """

    def area(self):
        """ Raises an Exception """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Validates if value is integer """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
