#!/usr/bin/python3
"""Student to JSON with filter
    """


class Student():
    """ Defines a student info """

    def __init__(self, first_name, last_name, age):
        """ Builder of the Student class """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Returns a dictionary representation of a Student """

        new_dict = {}

        if attrs is None:
            return self.__dict__

        for attr in attrs:
            if attr in self.__dict__.keys():
                new_dict[attr] = self.__dict__[attr]

        return new_dict
