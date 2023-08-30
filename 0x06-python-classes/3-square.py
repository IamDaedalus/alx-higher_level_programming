#!/usr/bin/python3

"""This is an empty class that will be built upon
to help create a new Square object to used in our program.

As time goes on we'll expand on it's methods and fields so
that over time it becomes more and more useful
"""

class Square:
    """This class defines a square with private instance attribute 'size'"""
    def __init__(self, size=0):
        """This method initialises a new class Square
        with private attribute size

        Args:
            self: the instance of the class for Python
            size: the size of the Sqr as an int
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size


    def area(self):
        """Returns the area of the square"""
        return self.__size ** 2
