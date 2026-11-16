import random

# Read names from a file

with open("names.txt") as infile:
    names = [ line.strip() for line in infile ]

# Ask user to enter a number, then randomly choose that many names
# from the list, avoiding any duplicate choices
num_names = int(input("enter the number of name you want to pick: "))
for i in range(num_names):
    name = random.randname(names)
    print(name_1)
    

# Display the chosen names, one per line
