#!/usr/bin/env python3

def Print_Foret(Tab):
    for Ligs in Tab:
        print(Ligs)

#On recupere les donnees initiales
with open('Input.8') as file:
    Data = [i for i in file.read().strip().split("\n")]

Hauteur = len(Data)
Largeur = len(Data[0])
print(f"{Hauteur} vs {Largeur}")
#Print_Foret(Data)
print(f" ")

Foret = []
for i in range(Hauteur):
    Ligne = []
    for j in range(Largeur):
        Ligne.append(0)
    Foret.append(Ligne)

#Parcours horizontal .... 
for i in range(Hauteur) :
#De Gauche a Droite
    Ligne = Data[i]
    Min = Ligne[0]
    Foret[i][0] = 1
    for j in range(1,Largeur,1):
        if int(Ligne[j]) > int(Min):
            Foret[i][j] = 1
            Min = Ligne[j]
#Puis de Droite a Gauche
    Min = Ligne[Largeur-1]
    Foret[i][Largeur-1] = 1
    for j in range(Largeur-2,0,-1):
        if int(Ligne[j]) > int(Min):
            Foret[i][j] = 1
            Min = Ligne[j]

#Parcours Vertical .... 
for i in range(Largeur):
    Min = Data[0][i]
    Foret[0][i] = 1
    for j in range(1,Hauteur,1):
        if int(Data[j][i]) > int(Min):
            Foret[j][i] = 1
            Min = Data[j][i]
    Min = Data[Hauteur-1][i]
    Foret[Hauteur-1][i] = 1
    for j in range(Hauteur -2,0,-1):
        if int(Data[j][i]) > int(Min) :
            Foret[j][i] = 1
            Min = Data[j][i]

Resultat = 0
#Print_Foret(Foret)
for i in range(Hauteur):
    for j in range(Largeur):
        Resultat += Foret[i][j]
    
print(Resultat)
