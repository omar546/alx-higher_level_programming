#!/usr/bin/python3
"""4-from_json_string"""
import json


def from_json_string(my_str):
    """ Function to return an object from JSON

    Args:
        my_str: JSON

    Raises:
        Exception: when the string can't be decoded

    """
    return json.loads(my_str)
