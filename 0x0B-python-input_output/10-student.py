#!/usr/bin/python3

"""This module defines a class called
Student
"""


from collections.abc import AsyncGenerator


class Student:
    """This class defines a student with a first name,
    last name and age
    """
    def __init__(self, first_name, last_name, age):
        """Init the student class"""
        self.age = age
        self.last_name = last_name
        self.first_name = first_name

    def to_json(self):
        """Returns the "json" serialised representation
        of this class
        """
        return self.__dict__
