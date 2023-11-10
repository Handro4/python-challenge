import os
import csv

# Step 1: Read the CSV File
file = "../Resources/budget_data.csv"
with open('budget_data.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip header row if present
    data = list(reader)

# Step 2: Initialize Variables
total_months = 0
net_total = 0
prev_month_profit = int(data[0][1])  # Assuming data is sorted by date
monthly_changes = []
greatest_increase = ["", 0]
greatest_decrease = ["", 0]

# Step 3-7: Loop Through the Data and Perform Calculations
for row in data:
    # Step 4: Calculate Total Number of Months and Net Total
    total_months += 1
    net_total += int(row[1])

    # Step 5: Calculate Monthly Changes
    monthly_change = int(row[1]) - prev_month_profit
    monthly_changes.append(monthly_change)
    prev_month_profit = int(row[1])

    # Step 8: Find Greatest Increase and Decrease
    if monthly_change > greatest_increase[1]:
        greatest_increase[0] = row[0]
        greatest_increase[1] = monthly_change
    if monthly_change < greatest_decrease[1]:
        greatest_decrease[0] = row[0]
        greatest_decrease[1] = monthly_change

# Step 6: Calculate Average Change
average_change = sum(monthly_changes) / len(monthly_changes)

# Step 8: Print the Results
print("Financial Analysis")
print("------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})")
print(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})")
