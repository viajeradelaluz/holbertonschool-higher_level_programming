#!/usr/bin/python3
""" Exact same object

Exams if an object is an instance of the specified class.
    """


def is_same_class(obj, a_class):
    """ Return if an object is instance of a class """
    if type(obj) is a_class:
        return True
    return False
