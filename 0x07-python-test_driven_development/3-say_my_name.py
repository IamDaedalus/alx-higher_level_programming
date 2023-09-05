#!/usr/bin/python3

"""This module prints the first and last name passed"""


def say_my_name(first_name, last_name=""):
    """This function prints the first and last name
    passed to this function

    Args:
        first_name: the first name as a string
        last_name: the last name as a string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
