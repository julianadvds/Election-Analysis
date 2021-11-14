import csv
import os

    #assign a variable to load the file from a path
file_to_load = os.path.join("Resources","election_results.csv")

    #assign a variable to save the file to a path
file_to_save = os.path.join("analysis","election_analysis.txt")

    # initialize a total vote counter
total_votes = 0
    
    # candidate options and votes
    # options is a list
candidate_options = []

    # candidate votes is a dictionary
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
    
    # iterate through the rows to calculate total votes, add up votes for each candidate based on the key
    for row in file_reader:
        
        # add to the total vote count
        total_votes +=1

        # print candidate name from each row
        candidate_name = row[2]

        # for each row, add candidate name to the candidate list, but only if it is not already in the list.
        if candidate_name not in candidate_options:
            
            #when the candidate_name is not in the list, add candidates name to candidate list
            candidate_options.append(candidate_name) 

            #begin tracking the candidate's vote count - actually adding to the votes will be later
            candidate_votes[candidate_name] = 0

        # for each row, use the candidates name as a key (it will already be in the list b/c of above if statement) and add a count for candidate's vote in the value
        candidate_votes[candidate_name] += 1

# All the tallying of data has been completed - moving to analysis and printing to excel. 

#save result to our text file  - open this file with the ability to write    
with open(file_to_save, "w") as txt_file:


        # after opening the file, print the final vote count to the terminal
    election_results = (
        f"\nElection Result\n"
        f"-------------------------\n"
        f"Total votes: {total_votes:,}\n"
        f"-------------------------\n"
    )
    print (election_results, end="")

  # save the final vote count to the text file
    txt_file.write(election_results)




    # determine the percentage of votes for each candidate by looping through the counts
    # iterate through the candidate list
        # for KEY in DICTIONARY
    for candidate_name in candidate_votes:
        
        # retrieve vote count of a candidate.
        votes = candidate_votes[candidate_name]

        # calculate percentage of votes
        vote_percentage = float(votes)/float(total_votes)*100
        
        
        #  To do: print out each candidate's name, vote count, and percentage of
        # votes to the terminal.
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        # print each candidate, their voter count and % to the terminal
      
      
        print(candidate_results)
        txt_file.write(candidate_results)

        # Determine winning vote count and candidate
        # Determine if the votes is greater than the winning count.
        if (votes>winning_count) and (vote_percentage> winning_percentage):
            # if true, then set winning_count = votes, winning_percentage = vote %
            winning_count = votes
            winning_percentage = vote_percentage

            # set the winning candidate equal to the candidates name
            winning_candidate = candidate_name

    # print winning candidate summary
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)

# print the final vote count to the terminal
    
    
    
  

