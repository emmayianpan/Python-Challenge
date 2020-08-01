import os
import csv
os.chdir(os.path.dirname(os.path.abspath(__file__)))
csvpath = os.path.join('.', 'Resources', 'budget_data.csv')

total_month = 0
total = 0
change = 0
profit = []
month = []
change_list = []

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    for row in csvreader:
        total_month += 1
        total = total + int(row[1])

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    sec_row = next(csvreader)
    pre_profit = int(sec_row[1])

    for row in csvreader:
        change = int(row[1]) - pre_profit
        pre_profit = int(row[1])

        change_list = change_list + [change]
        profit.append(change)
        month.append(row[0])

    increase = max(profit)
    increase_index = profit.index(increase)
    increase_month = month[increase_index]

    decrease = min(profit)
    decrease_index = profit.index(decrease)
    decrease_month = month[decrease_index]

    average = sum(change_list)/len(change_list)

print("Financial Analysis")
print("-----------------------------")
print(f"Total Months:{total_month}")
print(f"Total: ${total}")
print(f"Average Change: ${str(round(average,2))}")
print(f"Greatest Increase in Profits: {increase_month} (${str(increase)})")
print(f"Greatest Dncrease in Profits: {decrease_month} (${str(decrease)})")

output = (
    f"Financial Analysis\n"
    f"-----------------------------\n"
    f"Total Months:{total_month}\n"
    f"Total: ${total}\n"
    f"Average Change: ${str(round(average,2))}\n"
    f"Greatest Increase in Profits: {increase_month} (${str(increase)})\n"
    f"Greatest Dncrease in Profits: {decrease_month} (${str(decrease)})\n"
    )

with open("Analysis.txt",'w') as txt_file:
    txt_file.write(output)