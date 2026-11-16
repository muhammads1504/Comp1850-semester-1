# See README.md for instructions on what to do this program

import random

random.seed(3)

num1 = random.randint(1, 100)
num2 = random.randint(1, 100)
num3 = random.randint(1, 100)

print(num1, num2, num3)

#when a randon seed given therandom numbers proced by the random generator will be the same each time 
#but when commented out the generator will produce different numbers each time
