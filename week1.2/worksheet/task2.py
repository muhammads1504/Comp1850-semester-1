# Worksheet 1.2: Task 2 Solution
import sys
from util import read_numbers
numbers = read_numbers()
if not numbers:
    print("Error: no numbers provided")
    sys.exit()
minimum = min(numbers)
maximum = max(numbers)
mean = sum(numbers) / len(numbers) # the statistic mean function not used here because of the restrictio on the worksheet

in_order = sort.numbers() # this will sor the numebr is assending order
# after sorting we need to se how many numbers there are 
length_of_sorted = len(in_order)
#now wee need to find the middle number
middle_number = length_of_sorted/2
if length_of_sorted/2 == 1:
     median = numbers[middle_number]
