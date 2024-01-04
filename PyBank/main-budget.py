# Import module to read csv files, module to create path for operating systems
import csv
import os

# Load csv data from Resources 
Budget_file = os.path.join('Resources', "budget_data.csv")

# Create variables
TotalMonths = 0

TotalProfitLoss = 0

MonthOfYear = []

MonthlyPriceChange = []

BiggestProfit = ["", 0] 

BiggestLoss = ["", 9999999999999999999] 

# Read budget csv file from Resources folder
with open(Budget_file) as budget_data:
    budget = csv.reader(budget_data)

    # First header row
    HeaderRow = next(budget)

    # Code to process only first line of data 
    FirstRow = next(budget)
    TotalMonths += 1
    TotalProfitLoss += int(FirstRow[1])
    PrevEntry = int(FirstRow[1])  

    # Loop through rest of dataset
    for row in budget:

        # Number of months in data set and total profit/loss 
        TotalMonths += 1
        TotalProfitLoss += int(row[1])

        # Monthly change in Profit/Losses
        MonthlyChange = int(row[1]) - PrevEntry
        PrevEntry = int(row[1]) 

        # Update the lists
        MonthlyPriceChange += [MonthlyChange] 
        MonthOfYear += [row[0]]
       
        if MonthlyChange > BiggestProfit[1]:

            BiggestProfit[0] = row[0]
            BiggestProfit[1] = MonthlyChange

        if MonthlyChange < BiggestLoss[1]:

            BiggestLoss[0] = row[0]
            BiggestLoss[1] = MonthlyChange

# Average of monthly prices changes over time
MonthlyChange_Average = sum(MonthlyPriceChange) / len(MonthlyPriceChange)

# Print summary of data collected
Summary = (
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {TotalMonths}\n"
    f"Total Profit/Loss: ${TotalProfitLoss}\n"
    f"Average Change: ${MonthlyChange_Average:.2f}\n"
    f"Greatest Increase in Profits: {BiggestProfit[0]} (${BiggestProfit[1]})\n"
    f"Greatest Decrease in Profits: {BiggestLoss[0]} (${BiggestLoss[1]})\n"
    )


# Print results to Git Bash terminal 
print(Summary)

# Location in local repository to print results of data summary
output_file = os.path.join('Analysis', "budget_data_output.txt")

# Print data summary results to .txt file
with open(output_file, "w") as txt_file:

    txt_file.write(Summary)