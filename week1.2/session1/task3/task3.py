# Week 1.2, Session 1: Task 3
#lists can be changed and items can be inserted or removed
#whereas tuples cant be changed meaning no items can be added or removed
# both list and tuple can include both strings and integers
# with string being in "" and number just as

#we might not want to changed as that might cause bigger problem


fruit = ("apple", "banana", "cherry")
print(fruit)

# Find and display position of "banana"
print(fruit.index("banana"))
#show the position of specific items

# Display how many times "cherry" occurs
print(fruit.count("cherry"))

# Display how many times "strawberry" occurs
print(fruit.count("strawberry"))

# Unpack tuple into variables
#when we craete a tuple we pack the tuple by assigniong values to it
# but if we want to unpack the tuple we assign different value and print them
# if we want to do something with the tuple we have to unpack it

(green, yellow, red) = fruit # we have to put it this way around for this to work
print(green) # the assigned value to apple is green it goes in order . this will now print apple
print(yellow)# this will print banana
print(red)# this will print cherry