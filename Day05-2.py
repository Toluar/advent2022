#!/usr/bin/env python3

#On recupere les donnees initiales
with open('Input.5') as file:
    Plateau,Instructions = [i for i in file.read().strip("\n").split("\n\n")]

Lignes = Plateau.split("\n")

Nb_Colonnes=int(Lignes[len(Lignes)-1][-2])
Tours = []
for t in range(Nb_Colonnes) :
    Tours.append(["-"] )

for j in range(len(Lignes)-1) :
    Ligne = Lignes[j]
    for i in range(Nb_Colonnes):
        ind = (i*4) + 1
        if Ligne[ind] != " ":
            Tours[i].append(Ligne[ind])

Liste_Instructions = Instructions.split("\n")
for instruction in Liste_Instructions:
    instruction = instruction.replace("move ","").replace(" from ",",").replace(" to ",",").split(",")
    Nb_Elements = int(instruction[0])
    Colone_depart = int(instruction[1])-1
    Colone_arrive = int(instruction[2])-1
    Caractere_a_deplacer = ["-"]
    for i in range(Nb_Elements):
        ind = i + 1
        Caractere_a_deplacer.append(Tours[Colone_depart][1])
        del Tours[Colone_depart][1]
    del Tours[Colone_arrive][0]
    Tours[Colone_arrive]=Caractere_a_deplacer+Tours[Colone_arrive]


Str=""
for i in range(Nb_Colonnes):
    Str += Tours[i][1]
print(Str)


