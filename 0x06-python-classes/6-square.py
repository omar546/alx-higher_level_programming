#!/usr/bin/python3
"""square class"""


class Square:
    """Create a square """
    def __init__(self, size=0, position=(0, 0)):
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

        if not isinstance(position, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(position) != 2 or not all(isinstance(v, int) for v in position):
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(num >= 0 for num in position):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    def area(self):
        """Calculates  area of a square
        Returns: area 
        """

        return (self.__size ** 2)

    @property
    def size(self):
        """get the value of `size`"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set value of `size`
        Args:
            value (int): value to set `size`
        Raise:
            TypeError: if `value` isn't an integer
            ValueError: if `value` is less than 0
        """

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if (value < 0):
            raise ValueError("size must be >= 0")

        self.__size = value

    @property
    def position(self):
        """get `position` value """
        return self.__position

    @position.setter
    def position(self, value):
        """Set the value of `position`
        Args:
            value (int): value to set `position`
        Raise:
            TypeError: position isn't a tupple or doesn't contain
                       2 elements or has negative integers
        """

        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2 or not all(isinstance(v, int) for v in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(num >= 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    def my_print(self):
        """Prints a square to stdout using Hashs"""
        if self.__size == 0:
            print()
            return

        for i in range(self.position[1]):
            print(i)
        for i in range(self.__size):
            for i in range(self.__position[0]):
                print(" ", end="")
            for i in range(self.__size):
                print("#", end="")
            print()
