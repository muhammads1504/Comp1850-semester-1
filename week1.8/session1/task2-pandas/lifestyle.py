import pandas as pd

data = pd.read_csv("lifestyle_data.csv")
#pd.read_csv(data)
print(data)
# What data type is `data` as output from the `read_csv()` method?
#this will return a data frame 
#in that we can put our list of objects and we can create multiple of them 
#before ending we can also create a index line 
# in this line we can have get our index to be anyhting and we can recxall those index later if we wish


# For each of the following pieces of information, try and use pandas to find the answer from the dataset in 'data'
# - You can open the csv file to see what data is available.
# - Use the pandas documentation to explore functions that you can use.
# - Leave your code under the comments.

# Find the total number of students

# Find the mean average GPA of the students
length = len(data["GPA"])# to get the total number of diffreent GPAs 
total = data["GPA"].sum()
average = round(total/length, 2)
print(average)

# Find the standard deviation of how much sleep students get per day
standard_deviation = round(data["Sleep_Hours_Per_Day"].std(), 2) # pandas function to find the standard deviation
print(standard_deviation)
# Find the maximum amount of study hours per day
maximum = round(data["Sleep_Hours_Per_Day"].max(), 2)
print(maximum)

# Sort the students by social hours per day ascending (lowest -> highest)
order = data.sort_values(by="Social_Hours_Per_Day") # by default the order is low to high
print(order)
#if we wanted in opposite order we would have to mention that assending is false


# Add a column 'Total_hours' which adds together all the Hours_Per_Day columns into one
#do the sum of each one add them together



# Filter all students with a 'high' stress level, and all the students with a 'low' stress level.
high_level = data[(data["Stress_Level"] == "High")]
print(high_level)
low_level = data[(data["Stress_Level"] == "Low")]
print(low_level)
# Can you work out whether having a higher stress level leads to a higher GPA?
