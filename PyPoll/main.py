# Input location
import os
import csv

#file location
file_to_read = os.path.join('Resources/PyPollPLData.csv')

print(file_to_read)

# # of total votes

total_votes = 0
vote_khan = 0
vote_correy = 0
vote_li = 0
vote_otooley = 0

# open w context
with open(file_to_read, newline="", encoding="utf-8") as elections:

    # store contents of csv in variable csv reader
    csv_reader = csv.reader(elections, delimiter=",")

    # skip the header labels
    header = next(csv_reader)

    # iterate through rows
    for row in csv_reader:

        # count voter ID
        total_votes +=1

        # Count names
        if row [2] == "Khan":
            vote_khan +=1
        elif row [2] == "Correy":
            vote_correy +=1
        elif row [2] == "Li":
            vote_li +=1
        elif row [2] == "O'Tooley":
            vote_otooley +=1

#creat dict
candidates = ["Khan","Correy","Li","O'Tooley"]
votes = [vote_khan,vote_correy,vote_li,vote_otooley]

# join lists and find winner
dict_candivotes = dict(zip(candidates,votes))
key = max(dict_candivotes, key=dict_candivotes.get)

#summarized
percent_khan = (vote_khan/total_votes) * 100
percent_correy = (vote_correy/total_votes) * 100
percent_li = (vote_li/total_votes) * 100
percent_otooley = (vote_otooley/total_votes) * 100

#printing
print(f"Election Results")
print(f"------------")
print(f"Total Votes: {total_votes}")
print(f"------------")
print(f"Khan: {percent_khan:.3f}% ({vote_khan})")
print(f"Correy: {percent_correy:.3f}% ({vote_correy})")
print(f"Li: {percent_li:.3f}% ({vote_li})")
print(f"O'Tooley: {percent_otooley:.3f}% ({vote_otooley})")
print(f"------------")
print(f"Winner: {key}")
print(f"------------")

# output
filepath = os.path.join("Analysis","Election_results_Summary.txt")
with open(filepath, "w") as file:
# write
    file.write(f"Election Results")
    file.write("\n")
    file.write(f"------------")
    file.write("\n")
    file.write(f"total votes: {total_votes}")
    file.write("\n")
    file.write(f"------------")
    file.write("\n")
    file.write(f"Khan: {percent_khan:.3f}%({vote_khan})")
    file.write("\n")
    file.write(f"Correy: {percent_correy:.3f}%({vote_correy})")
    file.write("\n")
    file.write(f"Li: {percent_li:.3f}%({vote_li})")
    file.write("\n")
    file.write(f"O'Tooley: {percent_otooley:.3f}%({vote_otooley})")
    file.write("\n")
    file.write(f"------------")
    file.write("\n")
    file.write(f"winner: {key}")
    file.write("\n")
    file.write(f"------------")
    file.close()