#!/usr/bin/python3
"""Defines a Square class"""


class Square:
    """Represents a square"""

    def __init__(self, size=0):
        """Initialize a new square

        Args:
            size(int): the size of the new square
        """
        self.__size = size
        if isinstance(self.__size, int):
            raise TypeError("size must be an integer")
        if self.__size < 0:
            raise ValueError("size must be >= 0")
