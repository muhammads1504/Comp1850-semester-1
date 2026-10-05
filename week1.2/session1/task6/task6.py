# Week 1.2, Session 1: Task 6

from pprint import pprint

# Create music database, as a dictionary of strings mapped to lists
# (keys are artist names, values are lists of album names)
music = {
    "Karun Aujla" : "Courtside"  "Wavy"  "5-7", # comma has to be added to be consider 
    "Dilgit" : "GOAT" "Water" "Tension",
    "Atif Aslam" : "Dil diya gallan"
}
# Pretty-print the data structure
pprint(music) # this will arrange the print in such a way that is easier to read
print(music)
# Display details of one album recorded by a specific artists
print(music.get("Karun Aujla"))