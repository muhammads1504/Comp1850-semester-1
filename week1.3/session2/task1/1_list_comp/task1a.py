# Week 1.3, Session 1: For loop equivalent to a list comprehension

animals = ['dog','cat','hamster','goldfish']

not_fish = [item for item in animals if item != 'goldfish']

print(not_fish)

for animals in animals:
    if animals != 'goldfish':
        print(animals)
# in thei sone it just want us to create a for loop for that info

animals = ['dog', 'cat', 'hamster', 'goldfish']
not_fish_2 = [item for item in animals if item != 'goldfish']
print(not_fish_2)
# write the equivalent for loop to create the not_fish list from animals
# print your result to verify it is the same