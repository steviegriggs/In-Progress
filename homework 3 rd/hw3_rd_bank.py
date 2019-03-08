import os
import csv

csvpath = os.path.join('PyBank.csv')

with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    #print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    #WANT TO DO:
    # 1) total number of months 
    # 2) net total amount of "Profit/Losses" over the entire period 
    # 3) average of the changes in "Profit/Losses" over the entire period
    # 4) greatest increase in profits (date and amount) over the entire period
    # 5) greatest decrease in losses (date and amount) over the entire period

  
    # months = total number of months
    # net_change is sum of second column which I think is answer to number 2


    months = 0
    net_change = 0 
    #delta_list = []
    for x in csvreader:
        months = months +1
        net_change = net_change + float(x[1])
        #delta_list.append(float(x[1].next())-float(x[1]))
    print(f"There are {months} months")
    print(f" the net total amount of profit/ loss is {net_change}")

   
   