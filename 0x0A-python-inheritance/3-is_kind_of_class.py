#!/usr/bin/python3
""" Same class or inherit from

Exams if an object is an instance of, or if the object
is an instance of a class that inherited from.
    """


def is_kind_of_class(obj, a_class):
    """ Return if an object is instance of a class """
    if isinstance(obj, a_class):
        return True
    return False
