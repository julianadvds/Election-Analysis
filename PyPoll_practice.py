import csv
import os
# Open the data file.

file_to_load = os.path.join("Resources","election_results.csv")
    #assign a variable for the file to load, and the path
with open(file_to_load) as election_data:
    print(election_data)

file_to_save = os.path.join("analysis","election_analysis.txt")
outfile = open(file_to_save, "w")
outfile.write("Hello world")
outfile.close

with open(file_to_save, "w") as txt_file:
    txt_file.write("Hellow World")


# election_data = open("Resources/election_results.csv", "r")
# election_data.close()

# Write down the names of all the candidates.
# Add a vote count for each candidate.
# Get the total votes for each candidate.
# # Get the total votes cast for the election.

#3.4.1

