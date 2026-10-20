# Worksheet 1.3: Task 1

L = int(input("Length of sequence: ")) # this should be your only input

sequence = [0]
visited = {0}
for k in range(1,L):
    prev = sequence[-1]
    ans = prev - k
    if ans>0 and ans not in visited:
        sequence.append(ans)
        visited.add(ans)
        k=+1
    else:
        ans = prev + k
        sequence.append(ans)
        visited.add(ans)
        k=+1
        
    

# Your code for the Recaman Sequence
# You should store the sequence in an appropriate data structure named 'sequence'


# You may wish to use further output for testing purposes while you develop your code

[print(item) for item in sequence]  # this method is reasonably independent of the choice of data structure

# The web page https://en.wikipedia.org/wiki/Recam%C3%A1n%27s_sequence shows about 80 numbers in the sequence