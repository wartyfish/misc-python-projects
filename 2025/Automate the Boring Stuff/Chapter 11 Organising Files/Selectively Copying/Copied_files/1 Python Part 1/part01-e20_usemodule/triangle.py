"""
triangle.py

A simple module that provides functions for basic right-angled triangle
calculations such as computing the hypotenuse and the area.

Functions:
    hypotenuse(a, b): Returns the hypotenuse given the other two sides.
    area(a, b): Returns the area of a right-angled triangle given the two perpendicular sides.

Attributes:
    __version__ (str): Version of the module.
    __author__ (str): Author of the module.
"""
from math import sqrt

__version__ = "1.0.0"
__author__ = "Jamie"

def hypotenuse(a, b):
    """Return the length of the hypotenuse of a right-angled triangle.

    Args:
        a (float): The length of one side.
        b (float): The length of the other side.

    Returns:
        float: The length of the hypotenuse.
    """
    return sqrt(a**2 + b**2)

def area(a, b):
    """Return the area of a right-angled triangle.

    Args:
        a (float): The length of one perpendicular side.
        b (float): The length of the other perpendicular side.

    Returns:
        float: The area of the triangle.
    """
    return 0.5 * (a * b)