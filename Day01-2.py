#!/usr/bin/env python3

#On recupere les donnees initiales
filin = open("Input.1", "r")

Elfes = {}
Nb_Elfes = 1
Elfes[Nb_Elfes] = 0

Max_Calories1 = 0
Max_Calories2 = 0
Max_Calories3 = 0
Max_Calories = 0

for i,LigneTmp in enumerate(filin):
    Ligne = LigneTmp.strip()
    if len(Ligne) > 0 :
        Calorie=int(Ligne)
        Elfes[Nb_Elfes] += Calorie
    else :
        if Elfes[Nb_Elfes] > Max_Calories1 :
            Max_Calories3 = Max_Calories2
            Max_Calories2 = Max_Calories1
            Max_Calories1 = Elfes[Nb_Elfes]
        else :
            if Elfes[Nb_Elfes] > Max_Calories2 :
                Max_Calories3 = Max_Calories2
                Max_Calories2 = Elfes[Nb_Elfes]
            else :
                if Elfes[Nb_Elfes] > Max_Calories3 :
                    Max_Calories3 = Elfes[Nb_Elfes]
            
        Nb_Elfes += 1
        Elfes[Nb_Elfes] = 0
        Max_Calories = Max_Calories1 + Max_Calories2 + Max_Calories3
            
print(f"max Calorie : {Max_Calories}")
