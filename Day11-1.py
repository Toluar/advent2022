#!/usr/bin/env python3

with open('Input.11') as file:
    Data = [i for i in file.read().strip().split("\n\n")]

Nb_Tour = 20

#Singe :
#   Nbr_Regard 
#   liste Items
#   Dividande
#   Vrai => Num Singe
#   Faux => Num Singe
#   Multiplication => Num ou 1
#   Addition => Num ou 0

#Liste_Singe[0->?]

# Pour chaque tour 
#   Singe.Regarde => 
#       Pour chaque item => Nbr Regard ++
#       POur chaque item => Multiplication et Addition
#       POur chaque item => Divise par 3
#       POur chaque item => Test avec envoi vers un autre singe
#       

# Quand nbr de tours OK
#       cherche les 2 singes les plus actifs
#       Resultat = NbrRegard Singe1 * NbrRegard Singe2

print(Data[0])
