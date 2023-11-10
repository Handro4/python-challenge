import os
import csv
csvpath = os.path.join("..", "Resources", "election_data.csv")

# Step 1: Read the CSV File
with open(csvpath) as csvfile:
    reader = csv.DictReader(csvfile)
    data = list(reader)

# Step 2: Initialize Variables
total_votes = len(data)
candidates = {}
winner = ""
max_votes = 0

# Step 3-4: Loop Through the Data and Perform Calculations
for row in data:
    candidate = row['Candidate']
    if candidate not in candidates:
        candidates[candidate] = 1
    else:
        candidates[candidate] += 1

    if candidates[candidate] > max_votes:
        max_votes = candidates[candidate]
        winner = candidate

# Step 5: Calculate Vote Percentages
percentages = {candidate: (votes / total_votes) * 100 for candidate, votes in candidates.items()}

# Step 6: Print the Results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate, votes in candidates.items():
    print(f"{candidate}: {percentages[candidate]:.3f}% ({votes})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

# Step 7: Export Results to a Text File
with open('election_results.txt', 'w') as output_file:
    output_file.write("Election Results\n")
    output_file.write("-------------------------\n")
    output_file.write(f"Total Votes: {total_votes}\n")
    output_file.write("-------------------------\n")
    for candidate, votes in candidates.items():
        output_file.write(f"{candidate}: {percentages[candidate]:.3f}% ({votes})\n")
    output_file.write("-------------------------\n")
    output_file.write(f"Winner: {winner}\n")
    output_file.write("-------------------------\n")

print("Results exported to 'election_results.txt'")
