# Week 1.3, Session 1: Task 5b

rivers = {
  "London": "Thames", 
  "Leeds": "Aire", 
  "Liverpool": "Mersey",
  "York": "Ouse"
}

# loop through the dict extracting key and value

for c, r in rivers.items(): # the c and r in this means city and river, it is a variable name that can be anything you want. this will print for city in rivers print that city and the river
    print(c, r)

for c in rivers.keys():
  print(c)

for r in rivers.values():
  print(r)
# create 2 further for loops to iterate: 1. just through the keys, 2. just through the values
# hint: we looked at built in function for dicts last session