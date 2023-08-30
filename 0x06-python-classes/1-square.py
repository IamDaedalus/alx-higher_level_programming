#!/usr/bin/python3

"""This class contains methods and attributes for
a creating a square, getting various properties about
it such as its position, size and area packaged in
a neat format
"""


class Square:
    """A square class that is defined with a private instance
    attribute, size
    """
    def __init__(self, size):
        """This method initialises a new class Square
        with private attribute size

        Args:
            size: the size of the Sqr as an int
        """
        self.__size = size
