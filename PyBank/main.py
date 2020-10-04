#import Modules
import os
import csv

#establish the path of csv file and assign to csvpath
csvpath = "C:/Users/cjbei/Desktop/Python-Challenge/PyBank/Resources/budget_data.csv"


#read csv file
with open(csvpath,"r") as csvfile:

    csvreader = csv.reader(csvfile)
    csv_header = next(csvfile)
    
    # print(f'header:{csv_header}')

    # creating lists for profit, months, profit change
    months =[]
    profit=[]
    profit_change=[]
   
    #loop through each row starting after the header
    for row in csvreader:
        months.append(row[0])
        profit.append(int(row[1])) 
        total_months = len(months) 
        total_profit=sum(profit)
       
    for r in range(1,len(profit)):
            profit_change.append((int(profit[r])-int(profit[r-1])))
            
            profit_loss_change= round(sum(profit_change)/len(profit_change),2)
            max_increase= max(profit_change)
            max_decrease= min(profit_change)
            
            month_of_increase=months[profit_change.index(max_increase)]
            month_of_decrease=months[profit_change.index(max_decrease)]
           

print("Financial-Analysis")
print("-----------------------")
print(f"Total Months:{total_months}")
print(f"Total: ${total_profit}")
print("Average Change:" + "$" + str(profit_loss_change))
print(f"Greatest Increase in Profits:{month_of_increase}(${max_increase})")
print(f"Greatest Decrease in Profits:{month_of_decrease}(${max_decrease})")