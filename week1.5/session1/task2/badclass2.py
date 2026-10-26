# Another bad class implementation

# What does the runtime error mean? the define self is not being using so the programme cisnt reaing the attribute x as it is not defined where thats x and y are coming from
# How do we fix the code? make sure you are using what you have defined

class Point:
    """
    A point in 2D space.
    """

    def __init__(self, x_coordinate, y_coordinate):
        """
        Creates a Point, given x & y coordinates.
        """
        self.x = x_coordinate
        self.y= y_coordinate


p = Point(1.5, 2.0)
print(p.x)
print(p.y)
