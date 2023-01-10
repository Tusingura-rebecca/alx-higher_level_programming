#!/usr/bin/python3
"""defining the function write_file"""


def write_file(filename="", text=""):
    """ writes a string to a text file and returns number of
    characters written """
    with open(filename, encoding="UTF-8", mode="w") as a_file:
        return a_file.write(text)
