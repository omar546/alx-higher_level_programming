#!/usr/bin/python3
"""Class square"""

from models.base import Base
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class (inherits) rectangle class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Constructor for the Square class attributes"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Gets the width"""
        return self.width

    @size.setter
    def size(self, value):
        """Sets the size of square"""
        self.width = value
        self.height = value

    def __str__(self):
        """String representaion for Square class"""
        str_res = ("[Square] ({}) {}/{} - {}"
                   .format(self.id, self.x, self.y, self.width))
        return str_res

    def area(self):
        """Returns the area of the square"""
        return self.width ** 2

    def to_dictionary(self):
        """
        Dictionary representation for the
        square class
        """
        _map = super().to_dictionary()
        _map["size"] = _map["width"]
        del _map["width"], _map["height"]
        return _map

    def update(self, *args, **kwargs):
        """
        Update Square class data(attrs)

        Args:
            *args(any): list of arguments
            **kwargs(any):
        """
        if not args and not kwargs:
            return
        if args:
            attributes = ["id", "size", "x", "y"]
            for i, j in enumerate(args):
                if i < len(attributes):
                    setattr(self, attributes[i], j)
        else:
            for k, v in kwargs.items():
                if hasattr(self, k):
                    setattr(self, k, v)
