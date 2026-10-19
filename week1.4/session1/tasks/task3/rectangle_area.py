
# function implementation

def rectangle_area(length, width ):  # define suitable input data
    """#
    ask the user to enter the length and the width of the rectangle #
    """# implement the function

    #length =  int(input("enter the length of your rectangle: "))
    #width = int(input("enter the length of your rectangle: "))
    rectangle_area = length * width

    return    rectangle_area
    # return an appropriate value

# testing the function

# there are differnt ways of  writing the same code and both will return  the same ans
# in the first one you have to put in the 2 number in the code and the arithmatic operation is performed there

print(f"Area is {rectangle_area(3,2)}")   # provide suitable data matching your inputs

def rectangle_area( ):  # define suitable input data
    """#
    ask the user to enter the length and the width of the rectangle #
    """# implement the function

    length =  int(input("enter the length of your rectangle: "))
    width = int(input("enter the length of your rectangle: "))
    rectangle_area = length * width

    return    rectangle_area
    # return an appropriate value

# testing the function

print(f"Area is {rectangle_area()}")