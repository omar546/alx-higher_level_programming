#!/usr/bin/python3
"""9-student.py"""


class Student:
    """ Class that creates a student instances """

    def __init__(self, first_name, last_name, age):
        """ Special method to initialize """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ Method to return description of directory """
        return self.__dict__.copy()
