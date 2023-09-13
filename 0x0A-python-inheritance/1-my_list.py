#!/usr/bin/python3

"""This module inherits from the list class"""


class MyList(list):
    """This class inherits from the list class"""
    def print_sorted(self):
        """This function prints a list sorted in ascending
        order
        """
        self.sort()
        print(self)
