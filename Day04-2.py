#!/usr/bin/env python3

#On recupere les donnees initiales
with open('Input.4') as file:
    Data = [i for i in file.read().strip().split("\n")]

#print(Data)
Resultat=0

for pair in Data:
    Elfe1,Elfe2 = pair.split(",")
    Elfe1 = Elfe1.split("-")
    Elfe2 = Elfe2.split("-")
    Min1 = int(Elfe1[0])
    Max1 = int(Elfe1[1])
    Min2 = int(Elfe2[0])
    Max2 = int(Elfe2[1])

    if Min1 in range(Min2,Max2+1) or Max1 in range(Min2,Max2+1):
        Resultat += 1
#        print(f"{Min1}-{Max1},{Min2}-{Max2}")
    elif Min2 in range(Min1,Max1+1) or Max2 in range(Min1,Max1+1):
        Resultat += 1
#        print(f"{Min1}-{Max1},{Min2}-{Max2}")
print(Resultat)
