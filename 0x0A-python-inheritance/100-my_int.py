#!/usr/bin/python3
""" MyInt module"""


class MyInt(int):
    """ class MyInt that inherits from int"""

    def __eq__(self, other):
        """ equal to negation """

        return not super().__eq__(other)

    def __ne__(self, other):
        """ negation to equal """

        return not super().__ne__(other)
