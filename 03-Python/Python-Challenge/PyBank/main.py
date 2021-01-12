import os
import csv

# Path to collect data from Resources folder
budget_csv = os.path.join('Resources','budget_data.csv')

# Open File
with open(budget_csv, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter =',')
    print(csvreader)
    header = next(csvreader)

    #Begin analysing data 
    revenue_date = []
    revenue = []
    changes = []
    months = 0
    totalprofit = 0
    startprofit = 0

    #Calculation of dataset
    for row in csvreader:
        revenue_date.append(row[0])
        revenue.append(row[1])
        months = months + 1

    #Calculation average profit from data file)
        finalprofit = int(row[1])
        monthlyprofit = finalprofit - startprofit
        changes.append(monthlyprofit)
        totalprofit = totalprofit + monthlyprofit
        startprofit = finalprofit


    totalrevenue = 0

    count = months - 1
    averagechng = round((totalprofit) / (count))

#Loop through data in file
for x in revenue:
    totalrevenue += int(x)


# Find Maximum Profit and Minimu,m Profit from data file
greatestinc = max(changes)
greatestincmonth = revenue_date[changes.index(greatestinc)]
greatestdec = min(changes)
greatestdecmonth = revenue_date[changes.index(greatestdec)]


# Print results to terminal
print("\n---------------------------")
print("Financial Analysis")
print("---------------------------") 
print("Total Months: " + str(months))
print(f"Total: $ {totalrevenue}")
print(f"Average Change: $ {averagechng}")
print(f"Greatest Increase in Profits: {greatestincmonth} {greatestinc}")
print(f"Greatest Decrease in Profits: {greatestdecmonth}  {greatestdec}")
print("---------------------------")

# Print results to file

file = open('Analysis/Financial_Analysist.txt','w')

file.write("\n---------------------------\n")
file.write("Financial Analysis         \n")
file.write("\n---------------------------\n")
file.write("Total Months: " + str(months) +  "\n")
file.write("Total: $ " + str(totalrevenue) +  "\n")
file.write("Average Change: $ " + str(averagechng) +  "\n")
file.write("Greatest Increase in Profits: " + str(greatestincmonth) + " $ " + str(greatestinc) +  "\n" )
file.write("Greatest Decrease in Profits:  " + str(greatestdecmonth) + " $ " + str(greatestdec) +  "\n")
file.write("\n---------------------------\n")


#file.close()