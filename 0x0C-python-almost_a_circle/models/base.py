#!/usr/bin/python3
"""Base class"""

import json
import os


class Base:
    """the base class is the base of all shapes

    Note:
        The class is used to manage id attribute
        in all your future shapes classes
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
        """
        creates the JSON string representation
        for list_dictionaries

        Args:
            list_dictionaries (list): some of dictionaries

        """
        if list_dictionaries is None or list_dictionaries == " ":
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Save the string representation of
        Json list_objs to file

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
        """Decode the string
        representation json_string into list

        Args:
            json_string (str): A string from list
            of dictionaries

        """
        if json_string is None:
            return []
        if json_string == [] or not isinstance(json_string, str):
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Creates an instance with all attributes pre-set

        Args:
            **dictionary (pointer): a double pointer to a
            dictionary

        """
        default_width = 32
        default_height = 3 if cls.__name__ == "Rectangle" else 32
        result = cls(default_width, default_height)
        result.update(**dictionary)
        return result

    @classmethod
    def load_from_file(cls):
        """
        method to return a
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
