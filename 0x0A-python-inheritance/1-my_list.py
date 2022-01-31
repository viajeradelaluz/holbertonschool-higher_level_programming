#!/usr/bin/python3
""" My list

Contains the class MyList.
    """


class MyList(list):
    """ Define a class thar inherits from list """

    def __init__(self):
        """ Builder of the mylist class """
        super().__init__()

    def print_sorted(self):
        """ Order the list """
        list_copy = self.copy()
        list_copy.sort()
        print(list_copy)
