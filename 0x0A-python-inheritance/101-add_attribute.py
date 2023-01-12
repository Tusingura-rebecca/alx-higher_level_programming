#!/usr/bin/python3
"""module"""


def add_attribute(obj, attr, value):
    """adds a new attribute to an object if it’s possible
    Raise a TypeError exception
    """

    if hasattr(obj, '__dict__'):
        setattr(obj, attr, value)
    else:
        raise TypeError("can't add new attribute")
