import random

# Get user to input how many random numbers they want
numbers = int(input("enter how many random numebrs do you want: ")) # important thing is that the int function has to be before input.
# if put the other way around it will not work
for i in range(numbers):
    num1 = random.randint(1, 1000 ) # we must also give  range in order for this to work
    print(num1)

# Generate this many random numbers

# Write the random numbers to a file named random.txt, one number per line
with open("random.txt", "w") as f: f.write(str(num1))