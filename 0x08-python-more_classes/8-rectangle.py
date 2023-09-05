#!/usr/bin/python3

"""A module for creating a Rectangle"""


class Rectangle:
    number_of_instances = 0
    print_symbol = "#"
    """Class to create a new Rectangle instance"""
    def __init__(self, width=0, height=0):
        """Constructor method for our Rectangle class

        Args:
            width (int): the width of the rectangle as an int
            height (int): the height of the rectangle as an int
        """
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

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

    def area(self):
        """This method calculates the area of the Rectangle
        instance and returns it
        """
        return self.__height * self.__width

    def perimeter(self):
        """This method calculates the perimeter of the
        Rectangle instance and returns it
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__height * 2) + (self.__width * 2)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """This method compares two instances of the Rectangle
        class to find out which is bigger

        Args:
            rect_1 (Rectangle): the first rectangle
            rect_2 (Rectangle): the second rectangle
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if Rectangle.area(rect_1) > Rectangle.area(rect_2):
            return rect_1
        elif Rectangle.area(rect_1) < Rectangle.area(rect_2):
            return rect_2
        else:
            return rect_1

    def __str__(self):
        """This returns a visual representation of the Rectangle
        instance with # based on the height and width of the
        Rectangle
        """
        pattern = ""
        if self.__height == 0 or self.__width == 0:
            return pattern

        symbol = str(Rectangle.print_symbol)
        for _ in range(self.__height):
            pattern += symbol * self.__width + "\n"

        return pattern[:-1]

    def __repr__(self):
        """This returns the string representation of the Rectangle
        for debugging and evaluation purposes
        """
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """Prepare to meet your maker you Rectangle you"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
