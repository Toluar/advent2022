#!/usr/bin/env python3

with open('Input.10') as file:
    Data = [i for i in file.read().strip().split("\n")]

X = 1
i=0
Str = ""

for L in Data:
    i += 1
    if i > 40:
        i = 1
        print(Str)
        Str = ""
    if i in (X, X+1, X+2):
        Str += "#"
    else:
        Str += "."
    if L != "noop":
        Instr,Val = L.split(" ")
        i += 1
        if i > 40:
            i = 1
            print(Str)
            Str = ""
        if i in (X, X+1, X+2):
            Str += "#"
        else:
            Str += "."
        X += int(Val)
print(Str)


