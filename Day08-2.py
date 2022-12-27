#!/usr/bin/env python3

def Print_Foret(Tab):
    for Ligs in Tab:
        print(Ligs)

def Nbr_Arbres_Horizont(Tab, x,y,ind):
    Result = 0
    MaxTrouve = False
    i = x + ind
    while MaxTrouve == False:
#        print(f"{i},{y} : {Tab[y][i]}")
        if  int(Tab[y][i]) >= int(Tab[y][x]) :
            Result += 1
            MaxTrouve = True
        if int(Tab[y][i]) < int(Tab[y][x]) :
            Result += 1
        i = i + ind
        if i == Largeur or i == -1:
            MaxTrouve = True
    return Result


def Nbr_Arbres_Vert(Tab, x,y,ind):
    Result = 0
    MaxTrouve = False
    i = y + ind
    while MaxTrouve == False:
#        print(f"{i},{x} : {Tab[i][x]}")
        if  int(Tab[i][x]) >= int(Tab[y][x]) :
            Result += 1
            MaxTrouve = True
        if int(Tab[i][x]) < int(Tab[y][x]) :
            Result += 1
        i = i + ind
        if i == Hauteur or i == -1:
            MaxTrouve = True
    return Result



#On recupere les donnees initiales
with open('Input.8') as file:
    Data = [i for i in file.read().strip().split("\n")]

Hauteur = len(Data)
Largeur = len(Data[0])
#print(f"{Hauteur} vs {Largeur}")
#Print_Foret(Data)
#print(f" ")

Resultat = 0
for i in range(1,Largeur-1,1):
    for j in range(1,Hauteur-1,1):
        Position = int(Nbr_Arbres_Horizont(Data,i,j,-1))*int(Nbr_Arbres_Horizont(Data,i,j,1))*int(Nbr_Arbres_Vert(Data,i,j,-1))*int(Nbr_Arbres_Vert(Data,i,j,1))
        if Resultat < Position:
            Resultat = Position


print(Resultat)

