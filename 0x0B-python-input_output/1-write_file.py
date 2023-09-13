#!/usr/bin/python3

"""This module contains a function to write
to files
"""


def write_file(filename="", text=""):
    """This function writes some text to a file

    Args:
        filename: the filename and path
        text: the text to write to the file
    """
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
