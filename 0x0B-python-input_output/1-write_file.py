#!/usr/bin/python3
"""Write to a file

Contains the write_file method.
    """


def write_file(filename="", text=""):
    """ Returns the number of characters written """
    with open("my_first_file.txt", 'w', encoding='utf-8') as f:
        return f.write("This School is so cool!\n")
