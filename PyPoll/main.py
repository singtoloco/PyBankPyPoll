# -*- coding: utf-8 -*-
"""


@author: vvacharussiriyuth
"""
import os
import csv

#This method returns current working directory of a process.
print(os.getcwd())

csv_path = "election_data.csv"

with open(csv_path, newline='') as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter = ",")
    
    csv_header = next(csvreader)
#    print(f"CSV Header: {csv_header}")
    
    voter = []
    county = []
    candidate = []
    
    for row in csvreader:
        voter.append(row[0])
        county.append(row[1])
        candidate.append(row[2])

#The total number of votes cast
total_votes = len(voter)

#A complete list of candidates who received votes
candidate_unique = []
for x in candidate:
    if x not in candidate_unique:
        candidate_unique.append(x)    

#The total number of votes each candidate won
v_count = []
#The percentage of votes each candidate won
v_pct = []
str1 = ""

for y in candidate_unique:
    v_count.append(candidate.count(y))

v_pct = [z/total_votes for z in v_count]

for i in range(len(v_count)):
    str1 += (f"{candidate_unique[i]}: " + "{:.3%}".format(v_pct[i]) + f" ({v_count[i]})" '\n')
    
#The winner of the election based on popular vote.
max_votes = max(v_count)
i_max_votes = v_count.index(max_votes)
winner = candidate_unique[i_max_votes]

str_results = ("Election Results" '\n' "-------------------------" '\n'\
      f"Total Votes: {total_votes}" '\n' "-------------------------" '\n')
str2 = ("-------------------------" '\n'\
        f"Winner: {winner}" '\n'\
        "-------------------------" '\n')
str_results = str_results + str1 + str2
print(str_results)
    
#Wrie results to a file
text_file = open("PyPoll_results.txt", "w")
text_file.write(str_results)
text_file.close()