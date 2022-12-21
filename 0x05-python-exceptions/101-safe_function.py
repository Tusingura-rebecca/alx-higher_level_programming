#!/usr/bin/python3
import sys


def safe_function(fct, *args):
  try:
        result = fct(*args)
        return (result)
  except:
        print("Exception: {}".format(sys.exc_info()[]), file=sys.stderr)
        return (None)
