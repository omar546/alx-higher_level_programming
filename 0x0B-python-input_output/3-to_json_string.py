#!/usr/bin/python3
"""3-to_json_string"""
import json


def to_json_string(my_obj):
    """ Function to return the JSON representation of object

    Args:
        my_obj: object

    Raises:
        Exception: when the object can't be encoded

    """
    return json.dumps(my_obj)
