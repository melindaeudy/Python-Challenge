import os
import csv

# Path to collect data from Resources folder
election_csv = os.path.join('Resources','election_data.csv')

# Open File
with open(election_csv, 'r', newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter =',')
    print(csvreader)
    header = next(csvreader)
    
    Unique_Person = {}
    Percentage = {}
    winner_count = 0
    winner = ""
    voters = 0

        #Begin analysing data 

        #Calculation of dataset
        #Loop through data in file

    for row in csvreader:
        voters += 1
        if row[2] in Unique_Person.keys():
            Unique_Person[row[2]] += 1
        else: 
            Unique_Person[row[2]] = 1
    
    for key, value in Unique_Person.items():
        Percentage[key] = round((value/voters) * 100, 4)
        
    for key in Unique_Person.keys():
        if Unique_Person[key] > winner_count:
            winner = key
            winner_count = Unique_Person[key]

      
# Print results to terminal
print("\n---------------------------")
print("Election Results")
print("---------------------------") 
print("Total Votes:   " + str(voters))
print("---------------------------")
for key, value in Unique_Person.items():
    print(key + ": " + str(Percentage[key]) + "% (" + str(value) + ")") 
print("---------------------------")
print(f"Winner:  {winner}")
print("---------------------------")

# Print results to file

file = open('Analysis/Financial_Analysist.txt','w')

file.write("\n---------------------------\n")
file.write("Election Results    \n")
file.write("---------------------------\n") 
file.write("Total Votes:   " + str(voters) + "\n")
file.write("---------------------------\n") 
for key, value in Unique_Person.items():
        file.write(key + ": " + str(Percentage[key]) + "% (" + str(value) + ") \n")
file.write("---------------------------\n")
file.write("Winner: " + str(winner) +   "\n")
file.write("---------------------------\n")

#file.close()