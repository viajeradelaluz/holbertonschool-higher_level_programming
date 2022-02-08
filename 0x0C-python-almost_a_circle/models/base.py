#!/usr/bin/python3
"""Base class
    """

import json


class Base:
    """ Base class """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Builder of the Base class
            """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Returns a JSON string representation
            """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Writes the JSON presentation of list_objs
            """
        filename = "{}.json".format(cls.__name__)

        new_list = []
        if list_objs is not None and len(list_objs) > 0:
            for instance in list_objs:
                new_list.append(cls.to_dictionary(instance))

        with open(filename, 'w', encoding='utf-8') as f:
            f.write(cls.to_json_string(new_list))

    @staticmethod
    def from_json_string(json_string):
        """ Returns a list of JSON string representation
            """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ Returns an instance width the attributes updated
            """
        if cls.__name__ == "Rectangle":
            dummy = cls(2, 2)
        if cls.__name__ == "Square":
            dummy = cls(2)

        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """ Returns a list of instances
            """
        filename = "{}.json".format(cls.__name__)
        instance_list = []

        try:
            with open(filename, 'r', encoding='utf-8') as f:
                file_strs = cls.from_json_string(f.read())

            for instance in file_strs:
                instance_list.append(cls.create(**instance))

        except FileNotFoundError:
            pass

        return instance_list

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ Writes a CVS representation of list_objs
            """
        filename = "{}.csv".format(cls.__name__)
        new_list = []

        if list_objs is not None:
            for instance in list_objs:
                new_list.append(cls.to_dictionary(instance))

        with open(filename, 'w', encoding='utf-8') as f:
            f.write(cls.to_json_string(new_list))

    @classmethod
    def load_from_file_csv(cls):
        """ Returns a list of instances
            """
        filename = "{}.csv".format(cls.__name__)
        instance_list = []

        try:
            with open(filename, 'r', encoding='utf-8') as f:
                file_strs = cls.from_json_string(f.read())

            for instance in file_strs:
                instance_list.append(cls.create(**instance))

        except FileNotFoundError:
            pass

        return instance_list
