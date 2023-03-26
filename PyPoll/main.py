import os
import csv


election_csv = os.path.join("Resources", "election_data.csv")
Total_Votes = 0
Ballot_ID = []
Candidates = {}
Percentage = []


with open(election_csv) as electionfile:
    election_r = csv.reader(electionfile, delimiter=",")
    election_h = next(election_r)
    
    for row in election_r:
        Ballot_ID.append(int(row[0]))
        Total_Votes += 1
        
        U_candidate = row[2]
        
        if U_candidate not in Candidates:
            Candidates[U_candidate] = {"votes": 1, "percentage": 0}
            
        else:
            Candidates[U_candidate]["votes"] += 1
            
    for U_candidate in Candidates:
        Candidates[U_candidate]["percentage"] = round(Candidates[U_candidate]["votes"] / Total_Votes * 100, 2)
    
    winner = max(Candidates, key=lambda U_candidate: Candidates[U_candidate]["votes"])
    
output = (
    f"Election Results\n"
    f"-------------------------------------\n"
    f'Total Votes: {Total_Votes}\n'
    f"-------------------------------------\n"
    f'Charles Casper Stockham: Votes:({Candidates["Charles Casper Stockham"]["votes"]}), Percentage:{Candidates["Charles Casper Stockham"]["percentage"]}%\n'
    f'Diana DeGette: Votes:({Candidates["Diana DeGette"]["votes"]}), Percentage:{Candidates["Diana DeGette"]["percentage"]}%\n'
    f'Raymon Anthony Doane: Votes:({Candidates["Raymon Anthony Doane"]["votes"]}), Percentage:{Candidates["Raymon Anthony Doane"]["percentage"]}%\n'
    f"-------------------------------------\n"
    f'Winner of the Election: {winner}')
    
print(output)

output_file = os.path.join("Analysis", "Analysispp.txt")
with open("Analysispp.txt", 'w') as f:
    f.writelines(output)
