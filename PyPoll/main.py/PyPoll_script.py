import csv

# Filepath
file_path = r"C:\Users\eaalv\Bootcamp\python-challenge\PyPoll\Resources\election_data.csv"

# Variables
total_votes = 0
candidates = {}
winner = ""
winner_votes = 0

# Read in the CSV file
with open(file_path, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Read the header row
    header = next(csvreader)
    
    for row in csvreader:
        # Count total votes
        total_votes += 1
        
        # Track candidate votes
        candidate = row[2]
        if candidate not in candidates:
            candidates[candidate] = 1
        else:
            candidates[candidate] += 1

# Print results to the terminal
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")

# Calculate and print each candidate's total votes and percentage
for candidate, votes in candidates.items():
    percentage = round((votes / total_votes) * 100, 3)
    print(f"{candidate}: {percentage}% ({votes})")
    
    # Determine the winner
    if votes > winner_votes:
        winner = candidate
        winner_votes = votes

print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

# Export results to a text file
output_file_path = r"C:\Users\eaalv\Bootcamp\python-challenge\PyPoll\analysis\election_results.txt"
with open(output_file_path, 'w') as output_file:
    output_file.write("Election Results\n")
    output_file.write("-------------------------\n")
    output_file.write(f"Total Votes: {total_votes}\n")
    output_file.write("-------------------------\n")

    # Calculate and write each candidate's total votes and percentage
    for candidate, votes in candidates.items():
        percentage = round((votes / total_votes) * 100, 3)
        output_file.write(f"{candidate}: {percentage}% ({votes})\n")

    output_file.write("-------------------------\n")
    output_file.write(f"Winner: {winner}\n")
    output_file.write("-------------------------")
