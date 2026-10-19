# Week 1.3, Session 2: Sales Data Statistics

# We want to analyse a set of sales data in sales.csv
import csv

units_sold = []

with open("/workspaces/Comp1850-semester-1/week1.3/session2/task2/3_sales_data/sales.csv", "r", newline="") as file:
    reader = csv.reader(file)
    next(reader, None)  # skip header row (remove if your file has no header)

    for row in reader:
        if row:
            units_sold.append(int(row[3]))
            
if units_sold:
    largest_sale_day = max(units_sold)
else:
    largest_sale_day = None
    
if len(units_sold)>0:
    average_sale_amount = sum(units_sold)/len(units_sold)
    print(f"Largest_sale_day = {largest_sale_day}")
    print(f"Average_sale_amount = {average_sale_amount:.2f}")
else:
    print("invalid amount")

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