#!/usr/bin/python3
"""5-save_to_json_file.py"""
import json


def save_to_json_file(my_obj, filename):
    """ Function to write an object into a text file
    by JSON

    Args:
        my_obj: object
        filename: textfile name

    Raises:
        Exception: when the object can't be encoded

    """
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)
