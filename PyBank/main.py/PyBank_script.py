#1 Import
import os
import csv

#2 FilePath
csvpath = r"C:\Users\eaalv\Bootcamp\python-challenge\PyBank\Resources\budget_data.csv"

#3 Variables
total_months = 0
net_total = 0
previous_profit_loss = 0
profit_loss_changes = []
dates = []

#4 Read in the CSV file
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Read the header row
    header = next(csvreader)
    
    for row in csvreader:
        # Calculate total months
        total_months += 1
        
        # Calculate net total amount of "Profit/Losses"
        net_total += int(row[1])
        
        # Calculate changes in "Profit/Losses" over time and store in list for later average calculation
        change = int(row[1]) - previous_profit_loss
        profit_loss_changes.append(change)
        
        # Store the date
        dates.append(row[0])
        
        # Update previous profit/loss for the next iteration
        previous_profit_loss = int(row[1])

#5 Calculate average change
average_change = round(sum(profit_loss_changes[1:]) / (total_months - 1), 2)

#6 Find the greatest increase and decrease in profits
greatest_increase = max(profit_loss_changes)
greatest_increase_date = dates[profit_loss_changes.index(greatest_increase)]
greatest_decrease = min(profit_loss_changes)
greatest_decrease_date = dates[profit_loss_changes.index(greatest_decrease)]

#7 Print results to the terminal
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")

#8 Export results to a text file in "analysis" folder in PyBank 
output_file_path = r"C:\Users\eaalv\Bootcamp\python-challenge\PyBank\analysis\financial_analysis.txt"
with open(output_file_path, 'w') as output_file:
    output_file.write("Financial Analysis\n")
    output_file.write("----------------------------\n")
    output_file.write(f"Total Months: {total_months}\n")
    output_file.write(f"Total: ${net_total}\n")
    output_file.write(f"Average Change: ${average_change}\n")
    output_file.write(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n")
    output_file.write(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")
