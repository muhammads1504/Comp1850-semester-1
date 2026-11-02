# Worksheet 1.5: Rectangle Class

class Rectangle:
    """
    A rectangle, with a width and a height.
    """
    def __init__(self, width, height):
        """
        Creates a Rectangle, given values for width and height.
        """
        # Add code here to check type and value of provided width & height,
        # raising appropriate exceptions if necessary (see README.md)
        if not isinstance(width,(int or float)):
            raise TypeError("the width must be a number")
        if not isinstance(height, (int or float)):
            raise TypeError("height must be a number")
        if not isinstance(width<=0):
            raise ValueError("the width must be more than 0")
        if not isinstance(height<=0):
            raise ValueError("the height must be more than 0")
        
        self.width = width
        self.height = height
        
    # Implement methods is_square(), area() & perimeter() here
    # (See README.md for details of what they should do)
    def is_square(self):
        """
        will check if the width and height match and the given shape is a square
        """
        
        if self.width == self.height:
            return True
        else:
            return False
        
    def area(self):
        """
        will take the widht and height to calculate the area
        """
        
        area = self.width * self.height
        return area
    def perimeter(self):
        """
        adds all sides to find the perimeter of the rectangle
        """
        
        perimeter = (2*self.width) + (2*self.height)
        return perimeter