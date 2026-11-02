# Week 1.6, Session 1: Task 3

import math
from point import Point

VALID_COLOURS = {"red", "orange", "yellow", "green", "blue", "purple"}


class Shape:
    """
    Superclass for different types of shape.
    """

    def __init__(self, position, colour):
        """
        Creates a shape with the specified position & colour.
        """
        self.set_position(position)
        self.set_colour(colour)

    def set_position(self, position):
        """
        Moves this shape to the given position.
        """
        if not isinstance(position, Point):
            raise TypeError("position must be a Point")

        self.position = position

    def set_colour(self, colour):
        """
        Sets this shape's colour to the given colour.
        """
        if colour not in VALID_COLOURS:
            raise ValueError(f"invalid color: must be one of {VALID_COLOURS}")

        self.colour = colour


# Implement your Circle class here
# Make sure that it inherits properly from Shape!
class Circle:
    """
    sub class that will use Shapes class as superclass
    """
    def __init__(self, radius, position, colour):
        super().__init__(position)
        super().__init__(colour)
        self.radius = radius
        
        
    def set_radius(self, radius):
        if not isinstance(radius, int or float):
            raise TypeError("the radius must be a number")
        if radius<=0:
            raise ValueError("invalid number added for radius")
        return radius
    def __str__(self):
        """
        return the colour radius and the position of the circle in that order
        """
        return f"{self.colour} circle, radius {self.radius}, at {self.position}"
        
    def area(self):
        """
        return the area of the circle
        """
        return (math.pi * (self.radius)**2)
    def perimeter(self):
        """
        returns the perimeter of the circle
        """
        return math.pi * self.radius
        
            
            

