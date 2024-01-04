# Imports module to read csv files,  module to create path for operating system
import csv
import os

# Load csv from Resources folder
election_file = os.path.join("Resources", "election_data.csv")

# Create variables
VotesTotal = 0

Candidates = [] 

VotesByCandidate = {}

ElectionWinner = ""

WinnerVotes = 0

# Read election and process csv file from Resources folder
with open(election_file) as election_data:

    election = csv.reader(election_data)
    HeaderRow = next(election)

    # for loop run through vote tallies 
    for row in election:
        VotesTotal += 1

        # Initialize names of unique candidates and record votes for each
        if row[2] not in Candidates:  
            Candidates.append(row[2])  
            VotesByCandidate[row[2]] = 0   

        # Add up votes each candidate in the dictionary 
        VotesByCandidate[row[2]] = VotesByCandidate[row[2]] + 1

# loop through each candidate
for candidate in VotesByCandidate:

    Votes = VotesByCandidate.get(candidate)  
    vote_percentage = float(Votes) / float(VotesTotal) * 100

    # Determine the winner of election 
    if (Votes > WinnerVotes):
        WinnerVotes = Votes
        ElectionWinner = candidate

    # Output results to Git Bash Terminal 
    results_output = f"{candidate}: {vote_percentage:.3f}% ({Votes})\n"
    print(results_output)

# Print results 
Election_Results = (
    f"\n\nElection Results\n"
    f"-------------------------\n"
    f"Total Votes: {VotesTotal}\n"
    f"-------------------------\n"
    
    f"{candidate}: {vote_percentage:.3f}% ({Votes})\n")
print(Election_Results)

# Print summary of election winner to Terminal
Election_Results_Summary = (
    f"-------------------------\n"
    f"Winner: {ElectionWinner}\n"
    f"-------------------------\n")

print(Election_Results_Summary)

#  Election Candidates from terminal to txt file 
output_file = os.path.join("Analysis", "election_candidates.txt")

# Print results and export data to .txt file
with open(output_file, "w") as txt_file:

    # Save the final vote count 
    txt_file.write(results_output)

#  Election_Results from terminal to txt file 
output_file = os.path.join("Analysis", "election_results.txt")

# Print results and export data to .txt file
with open(output_file, "w") as txt_file:

    # Save the final vote count 
    txt_file.write(Election_Results)

# summary fo the Winning Candidate to .txt file
output_file = os.path.join("Analysis", "winning_candidate_summary.txt")

# Print results and export data to .txt file
with open(output_file, "w") as txt_file:

    # Save the winning candidate's name 
    txt_file.write(Election_Results_Summary)