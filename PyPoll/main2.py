
import os
import csv

election_data = "C:/Users/cjbei/Desktop/Python-Challenge/PyPoll/Resources/election_data.csv"


#assign variables and create lists
votes = []
candidates=[]
voterdict={}
percentage_votes=[]

with open(election_data) as csvfile:

    csvreader = csv.reader(csvfile)
    csv_header = next(csvreader)

    for row in csvreader:
        votes.append(row[0])
        candidates.append(row[2])
        total_votes= len(votes)

    for candidate in candidates:
        if candidate in voterdict:
            voterdict[candidate] += 1
        else:
            voterdict[candidate]=1
    
    votes_per_candidate= [x for x in voterdict.values()] 
    candidate_names=[x for x in voterdict.keys()] 
    for candidate in votes_per_candidate:
        percentage_votes.append((candidate/total_votes)*100)
   
   
    print("Election Result")
    print("----------------------")
    print(f"Total Votes: {str(total_votes)}")
    print("----------------------")
    for candidate in candidate_names:
        print(f'{candidate}:{percentage_votes[0]}% ({votes_per_candidate[0]})')
    print("----------------------")
    print(f"winner: {candidate_names(0)}")
    print("-----------------------")


 
 
