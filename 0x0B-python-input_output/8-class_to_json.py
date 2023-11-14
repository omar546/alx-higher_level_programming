#!/usr/bin/python3
"""8-class_to_json.py"""


def class_to_json(obj):
    """ Function to retun the dictionary for an object """

    result = {}
    if hasattr(obj, "__dict__"):
        result = obj.__dict__.copy()
    return result
