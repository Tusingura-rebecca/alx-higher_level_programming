#!/usr/bin/python3
"""
defines class MyList that inherits from list
"""


class MyList(list):

    """ prints sorted list """
    def print_sorted(self):
        print(sorted(self))
