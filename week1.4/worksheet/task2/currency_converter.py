
"""
    Portfolio Task - Week 4

    By submitting this code you are declaring that all work in this file,
    other than any provided template code, was written and developed by
    you independently.

    Name:
"""

def currency_converter(amount, from_currency, to_currency):

    conversion_rate = {
        'GBP': {'CNY': 9.24, 'PHP': 75.00, 'INR': 109.06},
        'CNY': {'GBP': 0.11, 'PHP': 8.12, 'INR': 11.81},
        'PHP': {'CNY': 0.12, 'GBP': 0.01, 'INR': 1.45},
        'INR': {'PHP': 0.69, 'CNY': 0.09, 'GBP': 0.01}
    }

    # your code here
    from_currency = from_currency.upper()
    to_currency = to_currency.upper()
    # first define what calculation need to be done and where the parts of the calc are coming from
    # we also need to check if the currency thats the user is entering is even present in the list
    if from_currency == to_currency:
        return round(float(amount),2)
    rate = conversion_rate[from_currency][to_currency]
    if amount<=0:
        return 0.0

    return round(amount*rate, 2)
     
     
amount = float(input("Enter the amount you want to convert: "))
from_currency = (input("Enter your from curency(GBP,CNY,PHP, or INR) : "))
to_currency = input("enter your to currency(GBP,CNY,PHP, or INR) : ")
your_amount = currency_converter(amount,from_currency , to_currency)
print(f"your converted amount is {your_amount:.2f}")
# Submit only this file currency_converter.py with the completed function.

# Remove any additional code you may have added during development and testing.