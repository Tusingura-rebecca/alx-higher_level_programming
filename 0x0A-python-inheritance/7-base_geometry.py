#!/usr/bin/python3
"""BaseGeometry class"""


class BaseGeometry:
    """Base Geometry class empty"""

    def area(self):
        """Area output"""

        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """ that validates value"""

        if not isinstance(value, int):
            raise TypeError(f'{name} must be an integer')
        if value <= 0:
            raise ValueError(f'{name} must be greater than 0')
