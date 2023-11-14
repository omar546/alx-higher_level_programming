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
