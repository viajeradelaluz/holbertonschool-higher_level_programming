#!/usr/bin/python3
"""Lookup

Find out a list of available attributes and methods of an object.
    """


def lookup(obj):
    """ Return the list of methods and attributes of an object """
    return dir(obj)
