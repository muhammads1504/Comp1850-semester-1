# Week 1.3, Session 2: Word Counter

# We want to read in a text file, and calculate how many words are in it. 
# You can use any of the .txt files to test this - or even make your own.

# open and read the file

file_to_count = input("Enter the file you want to be counted: ")
with open(f"/workspaces/Comp1850-semester-1/week1.3/session2/task2/1_word_counter/{file_to_count}","r") as infile:
    for line in infile:
        print(line)
total_words = 0
infile = [line.strip().split(",") for line in line]
 # this is a list comprehension that will strip the line of any whitespace and split it into a list of words using the comma as a delimiter
    # the strip function removes any whitespace from the start and end of the string, 
    #  the split function splits the string into a list of words, using the comma as a delimiter # so we can count the number of words in the list by using the len() function
for line in infile:
    total_words += len(line) # this will add the number of words in each line to the total word count
print(total_words)
# calculate the number of words
# hint: you could use .split() to break up by spaces
# hint: watch out for empty lines that might give you empty strings
# display the wordcount

# Here are the word counts you should get:
# story.txt - 290
# story2.txt - 326
# glasses.txt - 210