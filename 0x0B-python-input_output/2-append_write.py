#!/usr/bin/python3
"""2-append_write.py"""


def append_write(filename="", text=""):
    """ Function to append onto a text file

    Args:
        filename: filename
        text: text to write

    Raises
        Exception: when the file can be opened

    """

    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
