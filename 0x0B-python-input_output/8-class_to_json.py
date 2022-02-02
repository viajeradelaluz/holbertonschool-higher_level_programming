#!/usr/bin/python3
""" Class to JSON

Contains the class_to_json.
"""


def class_to_json(obj):
    """ Returns the dictionary description """
    return obj.__dict__
