# Input location
import os
import csv

# file location

file_to_read = 'Resources/PyBankPLData.csv'

# Create lists for variables

months = []
total_profit = []
monthly_profit_change = []

# open w context
with open(file_to_read, newline="", encoding="utf-8") as budget:

    # store contents of csv in variable csv reader
    csv_reader = csv.reader(budget)

    # skip the header labels
    header = next(csv_reader)

    # iterate through rows
    for row in csv_reader:

        # append total months and total profit
        months.append(row[0])
        total_profit.append(int(row[1]))

# iterate through rofits for profit change by month
for i in range(len(total_profit)-1):

    # difference added to change
    monthly_profit_change.append(total_profit[i+1]-total_profit[i])

# get max/min for profit change
largest_increase = max(monthly_profit_change)
largest_decrease = min(monthly_profit_change)

#recorrelate max/min to correct month
largest_increase_month = monthly_profit_change.index(largest_increase) + 1
largest_decrease_month = monthly_profit_change.index(largest_decrease) + 1

total_profit_sum = sum(total_profit)

total_months = len(months)

#printing
print("Financial Analysis")
print("--------------")
print("Months " + str(total_months))
print(f"Total Profit {total_profit_sum}")

# print(total: $(sum("total_profit"))
print(f"Average Change: {round(sum(monthly_profit_change)/len(monthly_profit_change),2)}")
print(f"Largest Profit Increase: {months[largest_increase_month]}(${(str(largest_increase))}")
print(f"Largest Profit Decrease: {months[largest_decrease_month]}(${(str(largest_decrease))}")

#output 1
output_file = 'Python-Challenge\PyBank\Financial_analysis.txt'
with open(output_file, "w") as file:

#output 2
    file.write("Financial Analysis")
    file.write("\n")
    file.write("--------------------")
    file.write("\n")
    file.write(f"Months: {len(months)}")
    file.write("\n")
    file.write(f"total: ${sum(total_profit)}")
    file.write("\n")
    file.write(f"Average Change: {round(sum(monthly_profit_change)/len(monthly_profit_change),2)}")
    file.write("\n")
    file.write(f"Greatest Increase in Profits: {months[max_increase_month]} (${(str(max_increase_value))})")
    file.write("\n")
    file.write(f"Greatest Decrease in Profits: {months[max_decrease_month]} (${(str(max_decrease_value))})")
    file.close()