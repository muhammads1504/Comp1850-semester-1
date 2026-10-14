# Week 1.3, Session 1: Task 2b

print("This program will repeat everything you type.")
print("To exit the program type quit")

while True:
    user_input = input("Say something: ")
    print(f"You said: {user_input}")
    if user_input == "quit":
        break
user_input = input("Say something: ")
while user_input != "quit":
    print(f"You said: {user_input}")
    
print(f"You said: {user_input}")


# As written the program has an infinite loop.
# Add a break statement so that if the user types 'quit' the program exits.