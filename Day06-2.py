#!/usr/bin/env python3

#On recupere les donnees initiales
with open('Input.6') as file:
    Data = [i for i in file.read().strip()]

NB_Caractere = 14


#print(Data)
Trouve = False
i = 0

while Trouve == False:
    print(f"--------------------")
    Test = Data[i:i+NB_Caractere]
    print(Test)
    Tmp = True
    for ind in range(NB_Caractere):
        Caractere = Test[ind]
        Test2 = []
        for j in range(NB_Caractere):
            if Test[j] != Caractere:
                Test2.append(Test[j])
        if len(Test2) < NB_Caractere -1 :
            Tmp = False

    i += 1
    Trouve = Tmp

    if i > len(Data):
        Trouve = True


print(i + NB_Caractere -1)

