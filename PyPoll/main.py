import os
import csv
os.chdir(os.path.dirname(os.path.abspath(__file__)))
csvpath = os.path.join('.', 'Resources', 'election_data.csv')

total_vote = 0
candidate = []
vote={}
name = []

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    for row in csvreader:
        total_vote += 1
        name = row[2]

        if name in vote:
            vote[name] = vote[name] +1
            candidate.append(name)
        else:
            vote[name] = 0

    khan_vote = vote["Khan"]
    correy_vote = vote["Correy"]
    li_vote = vote["Li"]
    otooley_vote = vote["O'Tooley"]

    khan = round((khan_vote/(total_vote))*100,2)
    correy = round((correy_vote/(total_vote))*100,2)
    li = round((li_vote/(total_vote))*100,2)
    otooley = round((otooley_vote/(total_vote))*100,2)
  
winner = max(vote, key=vote.get)

print("Election Results")
print("--------------------------------")
print(f"Total Votes: {total_vote}")
print("--------------------------------")
print(f"Khan: {khan}% ({khan_vote})")
print(f"Correy: {correy}% ({correy_vote})")
print(f"Li: {li}% ({li_vote})")
print(f"O'Tooley: {otooley}% ({otooley_vote})")
print("--------------------------------")
print(f"Winner: {winner}")
print("--------------------------------")

output = (
    f"Election Results\n"
    f"--------------------------------\n"
    f"Total Votes: {total_vote}\n"
    f"--------------------------------\n"
    f"Khan: {khan}% ({khan_vote})\n"
    f"Correy: {correy}% ({correy_vote})\n"
    f"Li: {li}% ({li_vote})\n"
    f"O'Tooley: {otooley}% ({otooley_vote})\n"
    f"--------------------------------\n"
    f"Winner: {winner}\n"
    f"--------------------------------\n"
    )

with open("Analysis.txt",'w') as txt_file:
    txt_file.write(output)