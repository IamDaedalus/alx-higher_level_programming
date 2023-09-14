#!/usr/bin/python3

"""Rectangle module that inherits from Base Geometry
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class that inherits from BaseGeometry"""
    def __init__(self, width, height):
        """Class instantiation method

        Args:
            width: the width of the new Rectangle
            height: the height of the new Rectangle
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
