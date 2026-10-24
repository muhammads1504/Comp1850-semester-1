# Week 4, Session 2: Task 1

# Write a function format_date that takes 4 arguments: day, month,
# year, separator. The separator is an optional argument with a default
# value to be "-". The function returns the formatted date as a string
# in the format day-month-year with the default separator.


def format_data(day = "Mon", month= "Jan", year="2026", separator="-"):
    formatted_date = f"{day}{separator}{month}{separator}{year}"
    # complete your code here

    return formatted_date
print(format_data("24","oct","2026","/"))
print(format_data("24","oct","2026","-"))
print(format_data("24","oct","2026",":"))

# Write code to test the function with separators such as "/", ":", "."
