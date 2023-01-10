#!/usr/bin/python3
"""defining read_file function"""


def read_file(filename=""):
    """reads text file UTF8 and prints it to stdout:"""
    with open(filename, encoding='utf-8') as my_file:
        for line in my_file:
            print(line, end="")
