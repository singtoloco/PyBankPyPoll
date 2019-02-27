# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 10:17:45 2019

@author: vvacharussiriyuth
"""

import pandas as pd
import numpy as np
import os

#This is temp path, will have to figure out later
#csv_path = "C:/Users/vvacharussiriyuth/OneDrive - Equitec Group, LLC/LNVshare/LNV BTS/csv/csv others/budget_data.csv"
#csv_path = "C:/Users/singt/NUCHI201902DATA1/Homework/03-Python/Instructions/PyBank/Resources/budget_data.csv"

#This method returns current working directory of a process.
print(os.getcwd())

#make sure we, on GitBash, cd to the parent folder of Resources before using ..
#Relative reference for filepath
#We can use os.path.join
csv_path = os.path.join('..', 'Resources', 'budget_data.csv')
#OR
#csv_path = "../Resources/budget_data.csv"
###The ".." means from current directory, go up one folder.


df_budget = pd.read_csv(csv_path)

#The total number of months included in the dataset
total_months = len(df_budget['Date'])

#The net total amount of "Profit/Losses" over the entire period
total_pnl = sum(df_budget['Profit/Losses'])

chg = []

for i in range(total_months-1):
    chg.append(df_budget.iloc[i+1][1] - df_budget.iloc[i][1])
    
#The average of the changes in "Profit/Losses" over the entire period
avg_chg = np.average(chg)

#The greatest increase in profits (date and amount) over the entire period
max_chg = max(chg)
i_max_chg = chg.index(max_chg)
month_max_chg = df_budget.iloc[i_max_chg+1][0]

#The greatest decrease in losses (date and amount) over the entire period
min_chg = min(chg)
i_min_chg = chg.index(min_chg)
month_min_chg = df_budget.iloc[i_min_chg+1][0]

#Print results to terminal
str_results = ("Financial Analysis" '\n' "----------------------------" '\n'\
      f"Total Months: {total_months}" '\n'\
      f"Total: ${total_pnl}" '\n'\
      f"Average  Change: ${avg_chg:.2f}" '\n'\
      f"Greatest Increase in Profits: {month_max_chg} (${max_chg})" '\n'\
      f"Greatest Decrease in Profits: {month_min_chg} (${min_chg})")

print(str_results)

#Wrie results to a file
text_file = open("PyBank_results.txt", "w")
text_file.write(str_results)
text_file.close()