# Week 1.2, Session 1: Task 4
# sets are not ordered so everytime we print the they migth give a complete different order


# these are example of set shown inside curly brackets
fruit = {"apple", "orange", "tomato"}
vegetables = {"leek", "tomato", "potato"}

# What do you think will be printed here?
#ans = this will print whatever comes in both of these
both = fruit.intersection(vegetables)
print(both)

# Why does the following code diplay five items?
#ans= because tomato come in both of them so is only printed once

food = fruit.union(vegetables)
print(food)# this print both in random order

# Add an item to fruit
fruit.add("cherry")
print(fruit) # this will again give a random order
# Remove an item from vegetables
vegetables.discard("potato")
print(vegetables)
# Find and display symmetric difference of the two sets
print(fruit.symmetric_difference(vegetables)) # this will print the difference in both that are not in the intersection