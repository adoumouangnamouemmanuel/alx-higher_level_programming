#!/usr/bin/python3
"""Defines a rectangle class."""


class Rectangle:
    """Represents a rectangle"""

    def __init__(self, width=0, height=0):
        """Initialize the rectangle object

        args:
            width(int): width of the rectangle
            height(int): height of the rectangle
        """

        self.width = width
        self.height = height

    @property
    def width(self):
        """get/set the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if not instance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """get/set the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if not instance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")