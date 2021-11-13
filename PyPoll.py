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

#winning candidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0


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
    
    
       #  To do: print out each candidate's name, vote count, and percentage of
    # votes to the terminal.
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")



    # Determine winning vote count and candidate
    # Determine if the votes is greater than the winning count.
    if (votes>winning_count) and (vote_percentage> winning_percentage):
        # if true, then set winning_count = votes, winning_percentage = vote %
        winning_count = votes
        winning_percentage = vote_percentage

        # set the winning candidate equal to the candidates name
        winning_candidate = candidate_name

winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)



