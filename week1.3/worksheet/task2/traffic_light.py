"""
Portfolio Task - Week 1.3
By submitting this code you are declaring that all work in this file, other than any provided template code, was written and developed by you independently.
Name: Muhammad Ahmed Kousar
"""

states = { "red":4, "red_amber":3, "green":5, "amber":3 }

systime = 0
maxtime = int(input("Enter the number of time you want the programme to run: ")) # read an integer number of steps (>0)

state = "red"
for time in range(systime, maxtime):
    rotation = time % 15  # will look at the remainders from the calculation
    if rotation <4:
        state = "red"
    elif rotation <7:
        state = "red_amber"
    elif rotation <12:
        state = "green"
    else:
        state = "amber"




    
    
        
        
        
        
print(f"Time {systime:03} State {state}")

# Simulate the traffic light system up to time=maxtime in 1-second steps

# At the end of each step you should output the time and state using the statement on line 14