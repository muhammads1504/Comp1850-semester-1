# Week 1.3, Session 2: Calculate Average Grade and Write to a File
import csv

with open("/workspaces/Comp1850-semester-1/week1.3/session2/task2/student_data.csv", "r") as infile:
    reader = csv.reader(infile)
    
    for row in reader:
        print(row)
    
# Open 'student_data.csv' to read each student's grades
# hint: skip the header row with data[1:]


# Read each student's grades and calculate their average grade
# hint: CSV data comes as strings, convert grade columns to int() for maths
# hint: student_data.csv has columns: ID, Name, Mathematics, Science, History
# hint: average = (maths + science + history) / 3


# Open a file called 'report.txt'
# Write each student's name and their average grade to the report
# hint: use 'w' mode to create a fresh report each time
# hint: format averages nicely, maybe to 2 decimal places with :.2f