#!/usr/bin/env python3

with open('Input.10') as file:
    Data = [i for i in file.read().strip().split("\n")]

X = 1
i=0
Resultat = 0

for L in Data:
    i += 1
    if i in (20, 60, 100, 140 , 180, 220):
        Resultat += X * i
    if L != "noop":
        Instr,Val = L.split(" ")
        i += 1
        if i in (20, 60, 100, 140 , 180, 220):
            Resultat += X * i
        X += int(Val)

print(Resultat)


