# -*- coding: utf-8 -*-
"""
@author: vvacharussiriyuth
"""
import os
import csv

#This method returns current working directory of a process.
print(os.getcwd())

csv_path = "budget_data.csv"

with open(csv_path, newline='') as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter = ",")
    
    csv_header = next(csvreader)
#    print(f"CSV Header: {csv_header}")
    
    date = []
    pnl = []
    
    for row in csvreader:
        date.append(row[0])
        pnl.append(row[1])

#The total number of months included in the dataset
total_months = len(date)

pnl = [int(i) for i in pnl]
#The net total amount of "Profit/Losses" over the entire period
total_pnl = sum(pnl)

chg = []

#for i in range(total_months-1):
for i in range(total_months-1):
    chg.append(pnl[i+1] - pnl[i])
    
#The average of the changes in "Profit/Losses" over the entire period
avg_chg = sum(chg)/(total_months-1)

#The greatest increase in profits (date and amount) over the entire period
max_chg = max(chg)
i_max_chg = chg.index(max_chg)
month_max_chg = date[i_max_chg + 1]

#The greatest decrease in losses (date and amount) over the entire period
min_chg = min(chg)
i_min_chg = chg.index(min_chg)
month_min_chg = date[i_min_chg + 1]


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