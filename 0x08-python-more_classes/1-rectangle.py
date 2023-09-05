#!/usr/bin/python3

"""A module for creating a Rectangle"""


class Rectangle:
    """Class to create a new Rectangle instance"""
    def __init__(self, width=0, height=0):
        """Constructor method for our Rectangle class

        Args:
            width (int): the width of the rectangle as an int
            height (int): the height of the rectangle as an int
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Property to get the width of the Rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter property to set the width of the
        Rectangle

        Args:
            value (int): the new value for the width of the
            Rectangle
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must >= 0")

        self.__width = value

    @property
    def height(self):
        """Property to get the height of the Rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter property to set the height of the
        Rectangle

        Args:
            value (int): the new value for the height of the
            Rectangle
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must >= 0")

        self.__height = value
