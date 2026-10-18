# Week 1.3, Session 2: Sales Data Statistics

# We want to analyse a set of sales data in sales.csv
import csv

units_sold = []

with open("/workspaces/Comp1850-semester-1/week1.3/session2/task2/3_sales_data/sales.csv", "r") as file:
    for line in file:
        print(line)
    for row in csv.reader(file):
        if row:
            units_sold.append(int(row[3]))
largest_sale_day = max(units_sold)
average_sale_amount = sum(units_sold)/len(units_sold)
print(f"Largest_sale_day = {largest_sale_day}")
print(f"Average_sale_amount = {average_sale_amount:.2f}")
# Open the file and read the data
# find the:
#   - largest sale day (highest sale amount)
#   - average sale amount
#   - the widget which has been sold the most
# and print these out in a nice, human-readable format


# additional: you can calculate other sales statistics such as:
# - total sales for each region
# - most sold widget for each region
# - total sales for each widget


# Hints:
# - Remember to handle file errors
# - The first row contains headers: Date, Product, Sales_Amount, Units_Sold, Region
# - Sales amounts are stored as strings - you'll need to convert to int() for math
# - For finding the highest selling widget, use a dictionary to count units sold per product
# - For average, sum all sales amounts and divide by number of rows