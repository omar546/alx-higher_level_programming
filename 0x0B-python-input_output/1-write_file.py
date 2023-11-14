#!/usr/bin/python3
"""1-write_file.py"""


def write_file(filename="", text=""):
    """ Function to write into a text file

    Args:
        filename: filename
        text: text to write

    Raises
        Exception: when the file can be opened

    """

    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
