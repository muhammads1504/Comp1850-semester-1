# Week 1.3, Session 1: Task 6b

values = [1,4,2,6,3,7]

print(values)

newval = []
for i in values:
    if i % 2 == 0:
        newval.append(2 * i)
    else:
        newval.append(i)

print(newval)

values = [1,4,2,6,3,7]
values = [2*i if i%2 == 0 else i for i in values ]
print(values)
# this help get a shorter form of all that
        

# write the list comprehension equivalent to the `for` loop

