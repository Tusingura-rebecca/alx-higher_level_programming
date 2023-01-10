#!/usr/bin/python3
"""defining function append_write"""


def append_write(filename="", text=""):
    """ appends a string to the end of text file and returns
    number of characters added """
    with open(filename, encoding="UTF-8", mode="a") as a_file:
        return a_file.write(text)
