import os
import csv


budget_data_csv = os.path.join("Resources", "budget_data.csv")

#set variables
month_counter = 0
total_pnl = 0
sum_pnl_change = 0
greatest_pnl_amount = -99999999
lowest_pnl_amount = 9999999999

#read csv
with open(budget_data_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
#skip first row
    header = next(csvreader)
#loop through each row
    for row in csvreader:
# two columns: "Date" and "Profit/Losses"
        date = row[0]
        pnl = int(row[1])
        total_pnl = total_pnl + pnl
# The total number of months included in the dataset
        month_counter = month_counter + 1
        if month_counter > 1:
            pnl_change = pnl - previous_pnl
# The net total amount of "Profit/Losses" over the entire period
# The changes in "Profit/Losses" over the entire period, and then the average of those changes
            sum_pnl_change = sum_pnl_change + pnl_change
# The greatest increase in profits (date and amount) over the entire period
            if pnl_change > greatest_pnl_amount:
                greatest_pnl_amount = pnl_change
                greatest_pnl_date = date
# The greatest decrease in profits (date and amount) over the entire period
            if pnl_change < lowest_pnl_amount:
                lowest_pnl_amount = pnl_change
                lowest_pnl_date = date
        previous_pnl = pnl

avg_pnl = round(sum_pnl_change/(month_counter-1),2)

output = (
f'Financial Analysis\n'
f'-----------------------\n'
f'Total Months: {month_counter}\n'
f'Total: ${total_pnl}\n'
f'Average Change: ${avg_pnl}\n'
f'Greatest Increase in Profits: {greatest_pnl_date} (${greatest_pnl_amount})\n'
f'Greatest Decrease in Profits: {lowest_pnl_date} (${lowest_pnl_amount})\n'
)
print(output)
# save the output file path
output_file = os.path.join("analysis","analysis.txt")

# open the output file, create a header row, and then write the zipped object to the csv
with open(output_file, "w") as datafile:
    datafile.write(output)