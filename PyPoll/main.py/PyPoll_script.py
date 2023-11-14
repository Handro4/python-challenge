#1 Import
import csv

#2 Filepath
file_path = r"C:\Users\eaalv\Bootcamp\python-challenge\PyPoll\Resources\election_data.csv"

#3 Variables
total_votes = 0
candidates = {}
winner = ""
winner_votes = 0

#4 Read in the CSV file
with open(file_path, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Read the header row
    header = next(csvreader)
    
    for row in csvreader:
        # Calculate total number of votes cast
        total_votes += 1
        
        # Calculate list of candidates who received votes
        candidate = row[2]
        if candidate not in candidates:
            candidates[candidate] = 1
        else:
            candidates[candidate] += 1

#5 Print results to the terminal
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")

#6 Calculate each candidate's percentage of votes and total number of votes won
for candidate, votes in candidates.items():
    percentage = round((votes / total_votes) * 100, 3)
    print(f"{candidate}: {percentage}% ({votes})")
    
    # Calculate the winner based on popular vote
    if votes > winner_votes:
        winner = candidate
        winner_votes = votes

print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

#7 Export results to a text file in 'analysis' folder in PyPoll
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
