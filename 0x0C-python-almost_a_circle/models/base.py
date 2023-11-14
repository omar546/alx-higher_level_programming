#!/usr/bin/python3
"""Base class"""

import json
import os


class Base:
    """Representing the base class

    Note:
        The class is used to manage id attribute
        in all your future classes and to avoid duplicating
        the same code (by extension, same bugs)
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize the class with an id

        Args:
            id (int): Class id

        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Produces the JSON string representation
        of list_dictionaries

        Args:
            list_dictionaries (list): A collection of dictionaries

        """
        if list_dictionaries is None or list_dictionaries == " ":
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Saves the JSON string representation of
        list_objs to a file

        Args:
            list_objs: A collection of instances inheriting from Base

        """
        if list_objs is None:
            with open(f"{cls.__name__}.json", "w") as file:
                file.write("[]")
        else:
            list_instance = [i.to_dictionary() for i in list_objs]
            with open(f"{cls.__name__}.json", "w") as file:
                file.write(cls.to_json_string(list_instance))

    @staticmethod
    def from_json_string(json_string):
        """Decodes the JSON string
        representation json_string into a list

        Args:
            json_string (str): A string depicting a list
            of dictionaries

        """
        if json_string is None:
            return []
        if json_string == [] or not isinstance(json_string, str):
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Generates an instance with all attributes pre-configured

        Args:
            **dictionary (pointer): Essentially a double pointer to a
            dictionary

        """
        default_width = 32
        default_height = 3 if cls.__name__ == "Rectangle" else 32
        result = cls(default_width, default_height)
        result.update(**dictionary)
        return result

    @classmethod
    def load_from_file(cls):
        """A class method returning a
        list of instances

        """
        list_instance = []
        file_name = f"{cls.__name__}.json"
        if os.path.isfile(file_name):
            with open(file_name, "r") as file:
                s = cls.from_json_string(file.read())
            for i in s:
                list_instance.append(cls.create(**i))
            return list_instance
        return []
