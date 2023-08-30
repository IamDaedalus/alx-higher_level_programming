#!/usr/bin/python3

"""This is an empty class that will be built upon
to help create a new Square object to used in our program.

As time goes on we'll expand on it's methods and fields so
that over time it becomes more and more useful
"""

class Square:
    """A square class that is defined with a private instance
    attribute, size
    """
    def __init__(self, size):
        """This method initialises a new class Square
        with private attribute size

        Args:
            self: the instance of the class for Python
            size: the size of the Sqr as an int
        """
        self.__size = size
