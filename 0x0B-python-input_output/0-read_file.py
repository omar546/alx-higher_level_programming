#!/usr/bin/python3
"""0-read_file.py"""


def read_file(filename=""):
    """ Function to read from file

    Args:
        filename: filename

    Raises
        Exception: when the file can be opened

    """

    with open(filename, 'r', encoding="utf-8") as f:
        read_data = f.read()
        print(read_data, end='')
