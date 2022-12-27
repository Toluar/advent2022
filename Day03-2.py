#!/usr/bin/env python3

#On recupere les donnees initiales
with open('Input.3') as file:
    Data = [i for i in file.read().strip().split("\n")]

#print(Data)
Somme = 0

j = 3
for i in range (0,len(Data),3):
    Phrases=Data[i:j]
    j = j+3
    for CodeAscii in range(1,53):
        if CodeAscii <27:
            Caractere=chr(CodeAscii+96)
        else:
            Caractere=chr(CodeAscii+64-26)

        if Caractere in Phrases[1] and Caractere in Phrases[2] and Caractere in Phrases[0]:
            CodeAscii=ord(Caractere)

#a = 97 => 1
#z = 122 => 26
#A = 65 => 27
#Z = 90 => 52
            if CodeAscii > 95 :
                Somme = Somme + CodeAscii -96
            else :
                Somme = Somme + CodeAscii -64 + 26

print(Somme)
