#!/usr/bin/env python3

#On recupere les donnees initiales
with open('Input.2') as file:
    Rounds = [i.replace(" ", "") for i in file.read().strip().split("\n")]

#Outcomes = {
#    "AX":4, "AY":8, "AZ":3, 
#    "BX":1, "BY":5, "BZ":9, 
#    "CX":7, "CY":2, "CZ":6 
#}


Outcomes = {
    "AX":3, "AY":4, "AZ":8, 
    "BX":1, "BY":5, "BZ":9, 
    "CX":2, "CY":6, "CZ":7 
}


Total_score = 0
for Round in Rounds:
    Total_score += Outcomes[Round]


# Answers
print(Total_score)
