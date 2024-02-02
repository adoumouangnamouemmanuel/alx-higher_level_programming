#!/usr/bin/python3
"""Defines the Square class"""


class Square:
    """Represents a square"""

    def __init__(self, size=0):
        """Initialize a new square

        Args:
            size(int): the size of the new square
        """
        self.size = size

    @property
    def size(self):
        """get/set the size of the square"""
        return self.__size

    @setter.size
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """compute the area of the square"""
        return (self.__size * self.__size)
