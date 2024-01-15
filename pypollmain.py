import csv
import pathlib
import os

# Open The File
with open('Resources/election_data.csv') as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")
    

    votes=[]
    Candidates=[]
    csv_header = next(csvfile)
    
#Read the file and loop through to find unique candidates
    for row in csvreader:
        votes.append(row)
        if row[2] not in Candidates:
            Candidates.append(str(row[2]))
    
# Calculate the total votes        
    Total_votes = len(votes)

#Calculate The Individual Candidate Votes
    Individual_votes = 0
    Candidate_votes=[]
    for Candidate in Candidates:
        #for vote in range(0 ,len(votes)):
        Individual_votes = 0
        for vote in votes:        
            if str(vote[2]) == Candidate:
                Individual_votes = Individual_votes +1
        Candidate_votes.append(Individual_votes)
        
#Calculate the percentage each candidate 
    percentage=[]
    for Candidate_vote in Candidate_votes:
        percent = (Candidate_vote / Total_votes ) * 100
        percentage.append(round(percent,3))

#Format the Display results 
    Print_lines=[]
    Print_lines.append("Election Results")
    Print_lines.append("------------------")
    Print_lines.append("Total Votes: "+ str(Total_votes))
    Print_lines.append("--------------------------")
    i=0
    for Candidate in Candidates:
        Print_lines.append(Candidate+" : "+str(percentage[i])+"% ("+str(Candidate_votes[i])+")")
        i=i+1
    Print_lines.append("--------------------------")
    winner_idx = percentage.index(max(percentage))
    Print_lines.append("Winner :"+Candidates[winner_idx])
    Print_lines.append("--------------------------")

with open("analysis/election_results.txt", "w") as file2:
    # Writing data to a file
    
    for Print_line in Print_lines:
        print(Print_line)
        file2.write("\n")
        file2.write(Print_line)
        
