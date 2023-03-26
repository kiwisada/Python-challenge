import os
import csv


budget_csv = os.path.join("Resources", "budget_data.csv")
Total_months = 0
Month = []
N_change = []
Net_change_pl = 0
Greatest_I = ["",0]
Greatest_D = ["", 999999999999]

with open(budget_csv) as budgetfile:
    budget_r = csv.reader(budgetfile, delimiter=",")
    budget_h = next(budget_r)
    
    First_row = next(budget_r)
    Total_months += 1
    Net_change_pl += int(First_row[1])
    Previous_n = int(First_row[1])
    
    for row in budget_r:
        
        Total_months += 1
        Net_change_pl += int(row[1])
        
        Net_change = int(row[1]) - Previous_n
        N_change.append(Net_change)
        Month.append(row[0])
        
        Average = round(int(Net_change) / len(N_change), 2) 
        
        if Net_change > Greatest_I[1]:
            Greatest_I[0] = row [0]
            Greatest_I[1] = Net_change
            
        if Net_change < Greatest_D[1]:
            Greatest_D[0] = row [0]
            Greatest_D[1] = Net_change

output = (            
    f"Analysis\n"
    f"Total months of months in data:{Total_months}\n"
    f"Net total amount of Profit/Losses over the entire period: ${Net_change_pl}\n"
    f"Average change of Profit/Losses over the entire period: ${Average}\n"
    f"Greatest increase in profits over the entire period: {Greatest_I[0]} ${Greatest_I[1]}\n"
    f"Greatest decrease in profits over the entire period: {Greatest_D[0]} ${Greatest_D[1]}")
print(output)

output_file = os.path.join("Analysis", "Analysispf.txt")
with open("Analysispf.txt", 'w') as f:
    f.writelines(output)
    
    