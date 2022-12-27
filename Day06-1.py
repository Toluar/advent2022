#!/usr/bin/env python3

#On recupere les donnees initiales
with open('Input.6') as file:
    Data = [i for i in file.read().strip()]

print(Data)
Trouve = False
i = 0

while Trouve == False:
    print(Data[i:i+4])
    Caractere1 = Data[i]
    Caractere2 = Data[i+1]
    Caractere3 = Data[i+2]
    Caractere4 = Data[i+3]

    Tab1 = [Caractere2,Caractere3,Caractere4]
    Tab2 = [Caractere1,Caractere3,Caractere4]
    Tab3 = [Caractere1,Caractere2,Caractere4]
    Tab4 = [Caractere1,Caractere2,Caractere3]

    Trouve1 = not(Caractere1 in Tab1)
    Trouve2 = not(Caractere2 in Tab2)
    Trouve3 = not(Caractere3 in Tab3)
    Trouve4 = not(Caractere4 in Tab4)
    
    Trouve = Trouve1 and Trouve2 and Trouve3 and Trouve4
    if Trouve == False:
        i += 1
    else :
        print(f"Trouve : {i} => {Data[i:i+4]} ")

print(i+4)
