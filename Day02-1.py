#!/usr/bin/env python3

#On recupere les donnees initiales
with open('Input.2') as file:
    Rounds = [i.replace(" ", "") for i in file.read().strip().split("\n")]

Outcomes = {
    "AX":4, "AY":8, "AZ":3, 
    "BX":1, "BY":5, "BZ":9, 
    "CX":7, "CY":2, "CZ":6 
}


Total_score = 0
for Round in Rounds:
    Total_score += Outcomes[round]


# Answers
print(Total_score)
