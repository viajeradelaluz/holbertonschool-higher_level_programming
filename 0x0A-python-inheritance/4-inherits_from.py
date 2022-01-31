#!/usr/bin/python3
""" Same class or inherit from

Exams if an object is an instance of a class that
inherited (directly or indirectly) from the specified class
    """


def inherits_from(obj, a_class):
    """ Return if an object is instance of a class """
    if type(obj) is a_class:
        return False
    return issubclass(type(obj), a_class)
