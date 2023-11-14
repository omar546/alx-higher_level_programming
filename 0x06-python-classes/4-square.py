#!/usr/bin/python3
"""square class"""


class Square:
    """Create a square """
    def __init__(self, size=0):
        """Init attributes
        Args:
            size (int): size of the square (side)
        Raises:
            TypeError: if `size` not integer
            ValueError: if `size` less than 0
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Calculates area of square
        Returns: area
        """

        return (self.__size ** 2)

    @property
    def size(self):
        """get value of `size`"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set value of `value`
        Args:
            value (int): value to set `value`
        Raise:
            TypeError: if `value` isn't an integer
            ValueError: if `value` is less than 0
        """

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if (value < 0):
            raise ValueError("size must be >= 0")

        self.__size = value
