#!/usr/bin/python3
"""inheritance checker"""


def inherits_from(obj, a_class):
    """ returns True if obj is an instance of a_class or a class inherited
    from a_class"""
    return issubclass(obj.__class__, a_class)
