#import packages
import os
import csv

#import statistics to calculate average, min and max
import statistics as st

#creating the listas to acumulate data
monthslist = []
amountlist = []
difference = []

#Path for data and final document
initialcsv = os.path.join("Resources", "budget_data.csv")
final = os.path.join("Analysis", "pybank_analysis.txt")

#open CSV
with open (initialcsv,'r') as csvfile:
    csvreader= csv.reader(csvfile, delimiter=',')
    Headers = next(csvreader)

    #to storage csv data in lists
    for row in csvreader:
        monthslist.append(row[0])
        amountlist.append(int(row[1]))

#create the loop to calculate total profit or losses
totalpl = 0
for i in amountlist:
    totalpl = totalpl + i

#insert a 0 in the first row so the table has the same lenght
difference.insert(0,0)

#to enter data to the difference list
for i in amountlist:
    difference.append(amountlist [i+1] - amountlist [i])

maxamount = max(difference)
minamount= min(difference)

#to find the date of the greatest increase and decrease
maxamountindex = difference.index(maxamount)
minamountindex = difference.index(minamount)  

maxdate = monthslist[maxamountindex]
mindate = monthslist[minamountindex]

#create average variable
averagepl = st.mean(difference)

#print all the information
Analysis_PyBank = (f"Financial Analysis\n"
                  f"----------------------------\n"
                  f"Total Months: {len(monthslist)}\n"
                  f"Total: ${totalpl}\n"
                  f"Average Change: ${round(averagepl,2)}\n"
                  f"Greatest Increase: {maxdate} (${int(maxamount)})\n"
                  f"Greatest Decrease: {mindate} (${int(minamount)})\n"  
)

print(Analysis_PyBank)

#print information in txt format
with open (final,'w') as textfile:
    textfile.write(Analysis_PyBank)
    

