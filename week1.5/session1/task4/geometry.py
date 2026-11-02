# Week 1.5, Session 1: Task 4

"""
Classes for working with two-dimensional geometry.
"""

import math


# Copy Point class definition here
class Point:
    """
    A point in 2D space.
    """

    def __init__(self, x, y):
        """
        Create a point with the x and y coordinates.
        """
        self.x = x
        self.y = y

    def distance(self):
        """
        Return the distance from the origin to this point.
        """
        return math.hypot(self.x, self.y)

    def distance_to(self, other): # the other in this means second point thats being put in to calculate the distance on that
        """
        Return the distance from this point to another Point.
        """
        dx = other.x - self.x
        dy = other.y - self.y
        return math.hypot(dx, dy)

# Copy Point class definition here

# Add a definition for a Circle class here, giving it
#  - A constructor that creates fields to represent the centre & radius
#    of a circle (assume centre is represented as a Point object)
#  - A method area(), returning the area of the circle
#  - A method perimeter(), returning the perimeter of the circle
class Circle:
    """
    Working with circle to find the area and parimeter in 2D
    """
    def __init__(self, x, y, radius, centre): # the radius must be before centre to say that the default value of the centre is 0,0
        """
        Create a point with the x and y coordinates and wroking to get the centre and radius
        """
        self.x = x
        self.y = y
        self.radius = radius
        self.centre = centre

    def area(self):
        """
        returns the area of the circle
        """ 
        return math.pi * (self.radius**2)
    def perimeter(self):
        """
        returns the perimetre of the circle
        """
        return math.pi * 2 * (self.radius)
# Don't add any testing code to this file!
