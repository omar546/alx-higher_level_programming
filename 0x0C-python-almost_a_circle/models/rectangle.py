#!/usr/bin/python3
"""Class Rectangle"""

from models.base import Base


class Rectangle(Base):
    """Rectangle class (inherits) the base class

    Args:
        Base(model): the model (inherited)

    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Constructor for the attributes

        Args:
            width(int): width
            height(int): height
            x(int): x (value)
            y(int): y (value)

        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter for the Width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for the Width of the rectangle

        Args:
            value(int): value of the width

        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter for the height of the rectangle"""
        return self.__height

    @width.setter
    def height(self, value):
        """Setter for the height of the rectangle

          Args:
            value(int): value of the height

        """
        if type(value) not in [int]:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def x(self):
        """Getter for x value"""
        return self.__x

    @x.setter
    def x(self, value):
        """
        Setter for x value

         Args:
            value(int): x value

        """
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getter for y value"""
        return self.__y

    @y.setter
    def y(self, value):
        """
        Setter for y value

         Args:
            value(int): y value

        """
        if type(value) not in [int]:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns the area of the rectangle"""
        return self.__height * self.__width

    def display(self):
        """Draws the Rectangle using hashs"""
        print("\n" * self.y,  end="")
        print((" " * self.x + "#" * self.__width + '\n') * self.__height, end="")

    def update(self, *args, **kwargs):
        """
        Update rectangle class data(attrs)

        Args:
            *args(args): list of arguments
            **kwargs(kwargs):

        """
        if not args and not kwargs:
            return
        if args is not None:
            attributes = ["id", "width", "height", "x", "y"]
            for i, j in enumerate(args):
                if i < len(attributes):
                    setattr(self, attributes[i], j)
        else:
            for k, v in kwargs.items():
                if hasattr(self, k):
                    setattr(self, k, v)

    def to_dictionary(self):
        """
        Dictionary representation for the
        rectangle class
        """
        _map = {}
        for key, value in self.__dict__.items():
            if key.startswith("_"):
                _map[key.split("__")[-1]] = value
            else:
                _map[key] = value
        return _map
    
    def __str__(self):
        """String representation for the rectangle class"""
        str_res = "[Rectangle] ({}) {}/{} - {}/{}"\
            .format(self.id, self.x, self.y, self.__width, self.__height)
        return str_res
