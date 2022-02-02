#!/usr/bin/python3
"""Student to JSON 
    """


class Student():
    """ Defines a student info """

    def __init__(self, first_name, last_name, age):
        """ Builder of the Student class """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ Returns a dictionary representation of a Student """
        return self.__dict__
