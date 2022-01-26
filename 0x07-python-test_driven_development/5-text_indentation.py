#!/usr/bin/python3
"""Text indentation

This module contains one function that indents a text.

    """


def text_indentation(text):
    """ Print two new lines after '.?:' characters """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    new_text = text

    for delim in ".?:":
        text_token_list = new_text.split(delim)

        new_text = ""
        for line in text_token_list:
            line = line.strip(" ")

            if new_text == "":
                new_text = line + delim
            else:
                new_text += "\n\n" + line + delim

    new_text = new_text[:-3]

    print(new_text, end="")
