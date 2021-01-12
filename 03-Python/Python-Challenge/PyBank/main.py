import os
import csv

# Path to collect data from Resources folder
budget_csv = os.path.join('..', 'Resources', 'budget_data.csv')

# Open File
with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter =',')
    print(csvreader)

#Begin analysing data by creating header row
csv_header = next(csvreader)
print("Financial Analysis")
print("---------------------------")

#Calculation of dataset
months = len(list(csvreader))
print("Total Months: " + str(months))
