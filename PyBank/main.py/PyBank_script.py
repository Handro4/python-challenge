import csv

# Define the file path
file_path = r"C:\Users\eaalv\Bootcamp\python-challenge\PyBank\Resources\budget_data.csv"

# Initialize variables
total_months = 0
net_total = 0
previous_profit_loss = 0
profit_loss_changes = []
dates = []

# Read the CSV file
with open(file_path, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Read the header row
    header = next(csvreader)
    
    for row in csvreader:
        # Count total months
        total_months += 1
        
        # Calculate net total profit/loss
        net_total += int(row[1])
        
        # Calculate change in profit/loss and store in list
        change = int(row[1]) - previous_profit_loss
        profit_loss_changes.append(change)
        
        # Store the date
        dates.append(row[0])
        
        # Update previous profit/loss for the next iteration
        previous_profit_loss = int(row[1])

# Calculate average change
average_change = round(sum(profit_loss_changes[1:]) / (total_months - 1), 2)

# Find the greatest increase and decrease in profits
greatest_increase = max(profit_loss_changes)
greatest_increase_date = dates[profit_loss_changes.index(greatest_increase)]
greatest_decrease = min(profit_loss_changes)
greatest_decrease_date = dates[profit_loss_changes.index(greatest_decrease)]

# Print results to the terminal
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")

# Export results to a text file
output_file_path = r"C:\Users\eaalv\Bootcamp\python-challenge\PyBank\analysis\financial_analysis.txt"
with open(output_file_path, 'w') as output_file:
    output_file.write("Financial Analysis\n")
    output_file.write("----------------------------\n")
    output_file.write(f"Total Months: {total_months}\n")
    output_file.write(f"Total: ${net_total}\n")
    output_file.write(f"Average Change: ${average_change}\n")
    output_file.write(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n")
    output_file.write(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")
