# Worksheet 1.2: Task 2 Solution
import sys
from util import read_numbers
numbers = read_numbers()
if not numbers:
    sys.exit("Error: no numbers provided")
minimum = min(numbers)
maximum = max(numbers)
mean = sum(numbers) / len(numbers) # the statistic mean function not used here because of the restrictio on the worksheet

in_order = sorted(numbers) # this will sor the numebr is assending order
# after sorting we need to se how many numbers there are 
length_of_sorted = len(in_order)
#now we need to find the middle number
middle_number = length_of_sorted//2 # this operator is used in truncating the division so it only gives the whole number
if length_of_sorted%2 == 1:
     median = in_order[middle_number]
else:
    middle_number_1 = (in_order[middle_number])
    middle_number_2 = (in_order[middle_number+1])
    median = (middle_number_1+middle_number_2)/2
    
print(f"Minimum = {minimum:.1f}")
print(f"Maximum = {maximum:.1f}")
print(f"Mean = {mean:.1f}")
print(f"Median = {median:.2f}")