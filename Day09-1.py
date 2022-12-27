#!/usr/bin/env python3

def PTab(Tab):
    for L in Tab:
        print(L)


Grille = []

IndX = 0
IndY = 0
MaxX = 0
MinX = 0
MaxY = 0
MinY = 0

#On recupere les donnees initiales
with open('Input.9') as file:
    Data = [f for f in file.read().strip().split("\n")]

for l in Data:
    Direction,Cases = l.split(" ")
    if Direction == "L" :
        IndX = IndX - int(Cases)
        if IndX < MinX :
            MinX = IndX
    if Direction == "R":
        IndX = IndX + int(Cases)
        if IndX > MaxX:
            MaxX = IndX
    if Direction == "U":
        IndY = IndY + int(Cases)
        if IndY > MaxY :
            MaxY = IndY
    if Direction == "D":
        IndY = IndY - int(Cases)
        if IndY < MinY:
            MinY = IndY


PlageX = (MinX * (-1)) + MaxX + 2
PlageY = (MinY * (-1)) + MaxY + 2

for i in range(PlageY):
    Ligne = []
    for j in range(PlageX):
        Ligne.append(0)
    Grille.append(Ligne)

IndHX = (MinX * (-1)) + 1
IndTX = (MinX * (-1)) + 1
IndHY = (MinY * (-1)) + 1
IndTY = (MinY * (-1)) + 1
Grille[IndHY][IndHX] = 1

print(f"Depart en {IndHX},{IndHY}")

for l in Data:
#    print(f"----------")
    Direction,Cases = l.split(" ")
#    print(f"{Direction} {Cases}")
    if Direction == "L":
        for X in range(IndHX,IndHX - int(Cases),-1):
            IndHX = IndHX - 1
            if abs(IndHX - IndTX) > 1:
                IndTX = IndHX + 1
                IndTY = IndHY
                Grille[IndTY][IndTX] = 1
    if Direction == "R":
        for X in range(IndHX,IndHX + int(Cases),1):
            IndHX = IndHX + 1
            if abs(IndHX - IndTX) > 1:
                IndTX = IndHX -1
                IndTY = IndHY
                Grille[IndTY][IndTX] = 1
    if Direction == "U":
        for Y in range(IndHY,IndHY + int(Cases),1):
            IndHY = IndHY + 1
            if abs(IndHY - IndTY) > 1:
                IndTY = IndHY -1
                IndTX = IndHX
                Grille[IndTY][IndTX] = 1
    if Direction == "D":
        for Y in range(IndHY,IndHY - int(Cases),-1):
            IndHY = IndHY - 1
            if abs(IndHY - IndTY) > 1:
                IndTY = IndHY +1
                IndTX = IndHX
                Grille[IndTY][IndTX] = 1
#    PTab(Grille)


Resultat = 0
for j in range(PlageY):
    for i in range(PlageX):
        Resultat += Grille[j][i]
print(Resultat)
