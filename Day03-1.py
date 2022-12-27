#!/usr/bin/env python3

#On recupere les donnees initiales
with open('Input.3') as file:
    Data = [i for i in file.read().strip().split("\n")]

#print(Data)
Somme = 0
for Line in Data:
    Longueur = int(len(Line)/2)
#    print(f"{Line} : {Longueur}")

    Moitie1 = set(Line[:Longueur])
    Moitie2 = set(Line[Longueur:])

    for Caractere in Moitie1:
        if Caractere in Moitie2:
            CodeAscii = ord(Caractere)
            #print(f"{Moitie1} Vs {Moitie2} : {Caractere} => {CodeAscii}")

#a = 97 => 1
#z = 122 => 26
#A = 65 => 27
#Z = 90 => 52
            if CodeAscii > 95 :
                Somme = Somme + CodeAscii -96
            else :
                Somme = Somme + CodeAscii -64 + 26

print(Somme)
