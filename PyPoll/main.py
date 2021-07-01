#import packages
import os
import csv

#creating the lists to acumulate data
votes = []
candidates = []

#Path for data and final document
initialcsv = os.path.join("Resources", "election_data.csv")
final = os.path.join("Analysis", "pypoll_analysis.txt")

with open(initialcsv, 'r') as pypolldata:
    pypollfinal = csv.reader(pypolldata, delimiter=",")
    Headers = next(pypollfinal)

#storage data in lists
    for row in pypollfinal:
        votes.append(row[0])
        candidates.append(row[2])

#calculate total votes
totalvotes = 0
for i in votes:
    totalvotes =   totalvotes + 1

#create variables to storage votes per candidate
khanvotes = 0
correyvotes = 0
livotes = 0
otooleyvotes = 0

#votes per candidate
for i in candidates:
    if (i == "Khan"):
        khanvotes = khanvotes + 1
    elif (i == "Correy"):
        correyvotes = correyvotes + 1
    elif (i == "Li"):
        livotes = livotes + 1
    else:
        otooleyvotes = otooleyvotes + 1

#calculate the percentage votes per candidate
khanpercentage = (khanvotes/totalvotes) * 100
correypercentage = (correyvotes/totalvotes) * 100
lipercentage = (livotes/totalvotes) * 100
otooleypercentage = (otooleyvotes/totalvotes) * 100

#create a list with the votes for each candidate to see winner
totalelection = [khanvotes, correyvotes, livotes, otooleyvotes]

#Find the winner votes and the name of the candidate
winnervotes = max(totalelection)

if winnervotes == khanvotes:
    winner = "Khan"
elif winnervotes == correyvotes:
    winner = "Correy"
elif winnervotes == livotes:
    winner = "Li"
elif winnervotes == otooleyvotes:
    winner = "O'Tooley"
else:
    winner = "No winner"


#print all the information
Analysis_PyPoll = (f"Election Results\n"
                  f"----------------------------\n"
                  f"Total Votes: {(totalvotes)}\n"
                  f"----------------------------\n"
                  f"Khan: {round(khanpercentage,1)}% ({khanvotes})\n"
                  f"Correy: {round(correypercentage,1)}% ({correyvotes})\n"
                  f"Li: {round(lipercentage,1)}% ({livotes})\n"
                  f"O´Tooley: {round(otooleypercentage,1)}% ({otooleyvotes})\n"
                  f"----------------------------\n"
                  f"Winner: {winner}\n"
                  f"----------------------------\n" 
)

print(Analysis_PyPoll)

#print information in txt format
with open (final,'w') as textfile:
    textfile.write(Analysis_PyPoll)