#!/usr/bin/python3
""" From JSON string to Object

Contains the from_json_string method.
    """

import json


def from_json_string(my_str):
    """ Returns an object represented by a JSON string """
    return json.loads(my_str)
