# Week 1.3, Session 2: Print PGM image info

# Open a pgm image file
# You can use the relative path ../images/filename
# You could handle file errors with try/except.
image = input("enter the image you want info about: " )

with open(f"/workspaces/Comp1850-semster-1/week1.3/task4/images/{image}", "r") as image_opened:
    

    
# Read the file content

# print image dimension (i.e., Dimensions: width x height pixels)

# print max gray value (i.e., Max Gray Value: max_gray_value)