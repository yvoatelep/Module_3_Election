# Data needed to retrieve
# 1) Total number of votes cast.
# 2) List of all cdidates who received votes
# 3) The percentage of votes each cadidate WON
# 4)Total number of votes each candidate won
#5) The winner of the election based on popular vote
import csv
import os
# Assign a variable for the file to load and the path
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to save the file to a path.
file_to_save = os.path.join("Analysis", "election_analysis.txt")

# Open the election results and read the file.

with open(file_to_load) as election_data:

# To do:read and analyze data here
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

# Read and print the header row.
    headers =next(file_reader)
    print(headers)


    # Print each row in the CSV file.
    for row in file_reader:
        print(row)

    # Print the file object
    print(election_data)

# Create a filename variable to a direct or indirect path to the file 
file_to_save = os.path.join("Analysis", "election_analysis.txt")
# Use the open statement to open file as a text file
with open(file_to_save, "w") as txt_file:
    # Write data to the file
    # txt_file.write("Counties in the Election\n------------------\nArapahoe\nDenver\nJefferson")
    txt_file.write("Counties in the Election\n------------------\nArapahoe\nDenver\nJefferson")
