# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 09:05:16 2019

@author: vvacharussiriyuth
"""

import pandas as pd
#import numpy as np
import os

#This is temp path, will have to figure out later
#csv_path = "C:/Users/vvacharussiriyuth/OneDrive - Equitec Group, LLC/LNVshare/LNV BTS/csv/csv others/election_data_sample.csv"
#csv_path = "C:/Users/singt/NUCHI201902DATA1/Homework/03-Python/Instructions/PyPoll/Resources/election_data.csv"

#This method returns current working directory of a process.
print(os.getcwd())

#make sure we, on GitBash, cd to the parent folder of Resources before using ..
#Relative reference for filepath
#We can use os.path.join
#csv_path = os.path.join('..', 'Resources', 'election_data.csv')
csv_path = "election_data.csv"
#OR
#csv_path = "../Resources/election_data.csv"
###The ".." means from current directory, go up one folder.

df_poll = pd.read_csv(csv_path)

##Testing duplicated by adding fake dup IDs
#df2 = df_poll.iloc[0:7][:]
#df_poll = df_poll.append(df2)

df_id_dup = df_poll[df_poll['Voter ID'].duplicated(keep=False)]

if df_id_dup.empty:
    print("Good, there are NO duplicated Voter IDs" '\n')
else:
    print("Warning!!!, there are duplicated Voter IDs" '\n')

#The total number of votes cast
total_votes = len(df_poll['Voter ID'])

#A complete list of candidates who received votes
#ref: https://stackoverflow.com/questions/32072076/find-the-unique-values-in-a-column-and-then-sort-them
""".unique() gives object??? and .drop_duplicate() is faster"""
##using .unique()
#list_candidates = df_poll.Candidate.unique() 

##using .drop_duplicate()
cdds = df_poll.Candidate.drop_duplicates()
##reset index for easier looping
cdds.reset_index(drop=True, inplace=True)
#print(type(cdds))
#print(cdds)

"""Counting votes of each candidate can be done in multiple ways as the followings"""
#len(df_poll[df_poll.Candidate == 'Khan'])
#df_poll[df_poll["Candidate"] == 'Khan'].count()["Candidate"]

v_count = []
v_pct = []
str1 = ""

for i in range(len(cdds)):
    v_count.append(len(df_poll[df_poll.Candidate == cdds[i]]))
    v_pct.append(v_count[i]/total_votes)
    str1 += (f"{cdds[i]}: " + "{:.3%}".format(v_pct[i]) + f" ({v_count[i]})" '\n')

#print(str1)
    
#Checking v
#if sum(v_count) !=  total_votes or sum(v_pct) != 1:
#    print("something is wrong!!!")
    
#The winner of the election based on popular vote.
max_votes = max(v_count)
i_max_votes = v_count.index(max_votes)
winner = cdds[i_max_votes]

#print ("{:.3%}".format(v_pct[0]))



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