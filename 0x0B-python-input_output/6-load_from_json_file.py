#!/usr/bin/python3
"""6-load_from_json_file.py"""
import json


def load_from_json_file(filename):
    """ Function to create an Object from JSON file

    Args:
        filename: text filename

    Raises:
        Exception: when the object can't be encoded

    """
    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)
