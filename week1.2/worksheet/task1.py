# Worksheet 1.2: Task 1 Solution
import sys
grade =(input("Enter your grade(0/100): "))
if not grade.isdecimal():
    sys.exit("Error: Grade must be an integer between 0 and 100")
result = int(grade)
if result<=39:
    print(f"{result} is a fail")
elif 40<=result<=69:
    print(f"{result} is a pass")
elif 70<= result <= 100:
    print(f"{result} is a distinction")
else:
    sys.exit("Error: Grade must be an integer between 0 and 100")