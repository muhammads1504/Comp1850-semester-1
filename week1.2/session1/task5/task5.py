# Week 1.2, Session 1: Task 5
#dictionaries
# in these we can use the keys to print out the values rather than using index to find something


rivers = {
    "London": "Thames",
    "Leeds": "Aire",
    "Liverpool": "Mersey"
}

print(rivers)

# Add two new entries to the rivers database
rivers["Punjab"]= "Indus"
print(rivers)
rivers["sindh"]="darya"
print(rivers)
# Display all the keys
print(rivers.keys()) # this will only give all the keys in the dict

# Display all the values
print(rivers.values())   # the empty braket after the keys and values is important for that to be printed
# Display all the key:value pairs, as tuples
print(rivers.items()) 
# Delete an entry from the rivers database
rivers.pop("London")
print(rivers)