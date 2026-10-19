# Week 1.3, Session 2: Write User Information to a File
name = input("Enter your name: ")
age = input("Enter your age: ")
favorite_colour = input("Enter your favorite colour: ")

with open("/workspaces/Comp1850-semester-1/week1.3/session2/task3/1_user_info/user_info.txt", "w") as file:
    file.write(f"Name: {name}\n")
    file.write(f"Age: {age}\n")
    file.write(f"Favorite Colour: {favorite_colour}\n")
# the n at the end of each line is for a new line, so that each piece of information is on a separate line in the file.

# Prompt the user for their name, age, and favorite colour.

# Open a file called 'user_info.txt' for reading

# Write each piece of information to the file, each on a new line.

# Hints:
# - Remember to add \n for new lines when writing to files


# Optional: extend this by using a loop to allow multiple people to enter their info in a row
# If you want multiple people to add info without overwriting, consider append mode 'a'
