#!/usr/bin/python3
"""class MyList that inherits from list""" 


class MyList(list):
    """mylist class inherits from the list class"""

    def print_sorted(self):
        """prints the list in a sorted fashion in a copied list"""

        sorted_list = self.copy()
        sorted_list.sort()
        print(sorted_list)
