#!/usr/bin/python3
"""defining read_file function"""


def read_file(filename=""):
    """reads filename with UTF8"""
    with open(filename, encoding='UTF8') as my_file:
    print(my_file.read(), end="")
