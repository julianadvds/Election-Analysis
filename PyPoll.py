import csv
import os

    #assign a variable for the file to load, and the path
file_to_load = os.path.join("Resources","election_results.csv")

    #assign a variable to save the file to a path
file_to_save = os.path.join("analysis","election_analysis.txt")

    # initialize a total vote counter
total_votes = 0
    
    # candidate options and votes
candidate_options = []
candidate_votes = {}
    
    # open the election results and read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    
    #read the header row
    headers = next(file_reader)

    # print each row in the csv file.
    for row in file_reader:
        
        # add to the total vote count
        total_votes +=1

        # print candidate name from each row
        candidate_name = row[2]

        # add candidate name to the candidate list.
        if candidate_name not in candidate_options:
            
            #add candidates name to candidate list
            candidate_options.append(candidate_name) 

            #begin tracking the candidate's vote count.
            candidate_votes[candidate_name] = 0

        candidate_votes[candidate_name] += 1

# determine the percentage of votes for each candidate by looping through the counts
# iterate through the candidate list
for candidate_name in candidate_votes:
    
    # retrieve vote count of a candidate.
    votes = candidate_votes[candidate_name]

    # calculate percentage of votes
    vote_percentage = float(votes)/float(total_votes)*100
    
    # print the candidates name and percentage of votes
    print(f"{candidate_name}: received {vote_percentage:.2f}% of the vote.")



#print the candidate list
# print (candidate_options)
# print(total_votes)
# print(candidate_votes)



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


