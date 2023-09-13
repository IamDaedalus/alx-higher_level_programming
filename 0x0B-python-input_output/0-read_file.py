#!/usr/bin/python3

"""This module helps read a file"""


def read_file(filename=""):
    """This function reads a file's contents and prints
    it to the terminal

    Args:
        filename: the path to the file
    """
    with open(filename, "r", encoding="utf-8") as file:
        buf = file.read()
        print(buf)
