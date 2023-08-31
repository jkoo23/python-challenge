import os
import csv

#import csv
election_data_csv = os.path.join("Resources", "election_data.csv")

total_votes = 0
candidates = []
candidate_votes = {}
win_votes = 0
win_cand = ''
output = f'Election Results\n'
output_file = os.path.join("analysis","analysis.txt")
line = f'-------------------------------\n'

with open(election_data_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)
#set variables for each column
    for row in csvreader:
#The total number of votes cast
        cand_name = row[2]
        total_votes = total_votes + 1
#A complete list of candidates who received votes
        if cand_name not in candidates:
                candidates.append(cand_name)
                candidate_votes[cand_name] = 0
#The total number of votes each candidate won
        candidate_votes[cand_name] = candidate_votes[cand_name] + 1                

#The percentage of votes each candidate won
print(output)
print(line)
print(f'Total Votes: {total_votes}\n')
print(line)

with open(output_file, "w") as datafile:
        datafile.write(output)
        line = f'-------------------------------\n'
        datafile.write(line)
        tot_votes = f'Total Votes: {total_votes}\n'
        datafile.write(tot_votes)
        datafile.write(line)
        for candidate in candidate_votes:
                votes = candidate_votes.get(candidate)
                percent_votes = round((votes/total_votes * 100), 3)
                results = f'{candidate}: {percent_votes}% ({votes})\n'
                # output.extend((f'{candidate}: {percent_votes}% ({votes})\n'))
                datafile.write(results)
                print(results)
        #The winner of the election based on popular vote
                if votes > win_votes:
                        win_votes = votes
                        win_cand = candidate
        winner = f'Winner: {win_cand}'
        print(line)
        print(winner)
        datafile.write(line)
        datafile.write(winner)