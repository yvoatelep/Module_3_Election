# Data needed to retrieve
# 1) Total number of votes cast.
# 2) List of all candidates who received votes
# 3) The percentage of votes each cadidate WON
# 4)Total number of votes each candidate won
#5) The winner of the election based on popular vote
import csv
from math import floor
import os
# Assign a variable for the file to load and the path
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to save the file to a path.
file_to_save = os.path.join("Analysis", "election_analysis.txt")

# 1. Initialize a total vote counter.
total_votes=0

#print the candidate name from each row
candidate_options = []

#declare the empty dictionary.
candidate_votes = {}

# # Winning Candidate and Winning Count Tracker
# winning_candidate = ""
# winning_count = 0
# winning_percentage = 0

# Open the election results and read the file.

with open(file_to_load) as election_data:

# To do:read and analyze data here
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

# Read and print the header row.
    headers =next(file_reader)
    # print(headers)


    # Print each row in the CSV file.
    for row in file_reader:
        #2 Add to the total vote count.
        total_votes += 1
        #Print the  candidate name from each row.
        candidate_name = row [2]
        #If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            # Add it to the candidate list. 
            candidate_options.append(candidate_name)
            # Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0
        #Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

        # Determine the percentage of votes for each candidate by looping through the counts.
# 1. Iterate through the candidate list.
for candidate_name in candidate_votes:
    # 2. Retrieve vote count of a candidate.
    votes = candidate_votes[candidate_name]
    # 3. Calculate the percentage of votes.
    vote_percentage = float(votes) / float(total_votes) * 100
    # 4. Print the candidate name and percentage of votes.
    print(f"{candidate_name}: received {vote_percentage:.1f}% of the vote.")

#print the cadidate vote dictionary. 
print(candidate_votes)

#Print the candidate list. 
print(candidate_options) 

#3 Print the total votes.
print(total_votes)

    #     print(row)

    # # Print the file object
    # print(election_data)

# # Create a filename variable to a direct or indirect path to the file 
# file_to_save = os.path.join("Analysis", "election_analysis.txt")
# # Use the open statement to open file as a text file
# with open(file_to_save, "w") as txt_file:
#     # Write data to the file
#     # txt_file.write("Counties in the Election\n------------------\nArapahoe\nDenver\nJefferson")
#     txt_file.write("Counties in the Election\n------------------\nArapahoe\nDenver\nJefferson")
