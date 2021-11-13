import csv
import os

    #assign a variable for the file to load, and the path
file_to_load = os.path.join("Resources","election_results.csv")

    #assign a variable to save the file to a path
file_to_save = os.path.join("analysis","election_analysis.txt")

    # open the election results and read the file
with open(file_to_load) as election_data:
    #to do: read and analyze the data here
    file_reader = csv.reader(election_data)
    print(file_to_load)

# read and print the header row.
    headers = next(file_reader)
    print(headers)
    



# # write three counties to the file
# with open(file_to_save, "w") as txt_file:
#     txt_file.write("Counties in the election\n")
#     txt_file.write(("-"*22))
#     txt_file.write("\nArapahoe\nDenver\nJefferson")


# Write down the names of all the candidates.
# Add a vote count for each candidate.
# Get the total votes for each candidate.
# # Get the total votes cast for the election.

#3.4.1

#import os


