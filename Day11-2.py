#!/usr/bin/env python3

with open('Input.11') as file:
    Data = [i for i in file.read().strip().split("\n\n")]

Nb_Tour_Max = 10000

class Singe:
    def __init__(self,Ind):
        self.Ind = Ind
        self.Nbr_Regard = 0
        self.Items = []
        self.Condition = 0
        self.COK = 0
        self.CKO = 0
        self.Multiplication = "1"
        self.Addition = "0"

Jungle = []
Modulo = 1

for Singes in Data :
    Def_S = Singes.split("\n")
    #On cree le singe ...
    S = Singe(Def_S[0].split()[1][0])

    # On rajoute les items
    S.Items = Def_S[1].replace("Starting items: ","").strip().split(", ")
    
    # et l operation a faire
    O = Def_S[2].replace("Operation: new = ","").split()
    if O[1] == '+':
        S.Addition = O[2]
    else:
        S.Multiplication = O[2]
    
    # Le test .... Divisible par .... 
    S.Condition = int(Def_S[3].replace("Test: divisible by ","").strip())
    Modulo = Modulo * S.Condition

    # Le singe si test OK ou KO : 
    S.COK = int(Def_S[4].replace("If true: throw to monkey ","").strip())
    S.CKO = int(Def_S[5].replace("If false: throw to monkey ","").strip())

    Jungle.append(S)

print(f"Modulo : {Modulo}")

for NbTour in range(Nb_Tour_Max):
    for Singes in Jungle:
        for i in range(len(Singes.Items)):
            Elm = int(Singes.Items[0])
            Singes.Nbr_Regard += 1
            if Singes.Addition == "0":
                if Singes.Multiplication.isdigit() :
                    Elm = Elm * int(Singes.Multiplication)
                elif Singes.Multiplication == "old":
                    Elm = Elm * Elm
            else:
                if Singes.Addition.isdigit() :
                    Elm = Elm + int(Singes.Addition)
                elif Singes.Addition == "old":
                    Elm = Elm + Elm
            Elm = Elm % Modulo
            if (Elm % Singes.Condition) == 0:
                Singes.Items.remove(Singes.Items[0])
                Jungle[int(Singes.COK)].Items.append(Elm)
            else: 
                Singes.Items.remove(Singes.Items[0])
                Jungle[int(Singes.CKO)].Items.append(Elm)

Max1 = 0
Max2 = 0
for S in Jungle:
    print(f"Singe {S.Ind} : {S.Nbr_Regard}")
    if S.Nbr_Regard > Max2 :
        Max2 = S.Nbr_Regard
    if S.Nbr_Regard > Max1 : 
        Max2 = Max1
        Max1 = S.Nbr_Regard

print(f"{Max1 * Max2}")
