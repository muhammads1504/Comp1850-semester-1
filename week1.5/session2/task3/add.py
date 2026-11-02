# Week 1.5, Session 2: Task 3

# Write a program here that creates two Money objects, prints them,
# then adds them together and prints their sum
class Money:
    
    def __init__(self, pounds, pence):
        """
        creates a money object with pounds and pence
        """
        if not isinstance(pounds, (int or float)):
            raise TypeError("the amounts in pounds must be a number")
        