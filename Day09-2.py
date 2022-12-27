#!/usr/bin/env python3

MaxMaillon = 9
FichierInput = "Input.9"

def PTab(Tab):
    for L in Tab:
        print(L)

def ClearTab(Tab,x,y):
    for i in range(y):
        for j in range(x):
            Tab[i][j] = 0


class Maillon:
    def __init__(self,Ind,DepX,DepY):
        self.Ind = Ind
        self.PosX = int(DepX)
        self.PosY = int(DepY)
        self.Suivant = []
        self.Precedent = []
        self.Grille = []

    def Add_Maillon(self,Nom):
        DepX = self.PosX
        DepY = self.PosY
        Maillon_tmp = Maillon(Nom,DepX,DepY)
        Maillon_tmp.Precedent.append(self)
        self.Suivant.append(Maillon_tmp)

    def PSTab(self):
        for L in self.Grille:
            print(L)

    def Horizontal(self,X):
        self.PosX = self.PosX + X
        self.Grille[self.PosY][self.PosX] = 1
        if self.Ind < MaxMaillon:
            PX = self.Suivant[0].PosX
            PY = self.Suivant[0].PosY
            if abs(self.PosX - PX) > 1 or abs(self.PosY - PY) > 1:
                if self.PosY == PY:
                    self.Suivant[0].Horizontal(X)
                if self.PosY > PY:
                    self.Suivant[0].Diagonale(X,1)
                if self.PosY < PY:
                    self.Suivant[0].Diagonale(X,int(-1))

    def Vertical(self,Y):
        self.PosY = self.PosY + Y
        self.Grille[self.PosY][self.PosX] = 1
        if self.Ind < MaxMaillon:
            PX = self.Suivant[0].PosX
            PY = self.Suivant[0].PosY
            if abs(self.PosX - PX) > 1 or abs(self.PosY - PY) > 1 :
                if self.PosX == PX:
                    self.Suivant[0].Vertical(Y)
                if self.PosX > PX:
                    self.Suivant[0].Diagonale(1,Y)
                if self.PosX < PX:
                    self.Suivant[0].Diagonale(int(-1),Y)

    def Diagonale(self,X,Y):
        self.PosX = self.PosX + X
        self.PosY = self.PosY + Y
        self.Grille[self.PosY][self.PosX] = 1
        if self.Ind < MaxMaillon:
            PX = self.Suivant[0].PosX
            PY = self.Suivant[0].PosY
            if abs(self.PosX - PX) > 1 or abs(self.PosY - PY) > 1 :
                if self.PosX == PX:
                    self.Suivant[0].Vertical(Y)
                if self.PosY == PY:
                    self.Suivant[0].Horizontal(X)
                if self.PosY != PY and self.PosX != PX:
                    self.Suivant[0].Diagonale(X,Y)
                    
    def Position(self,Grille):
        Grille[self.PosY][self.PosX] = self.Ind
        if self.Ind < MaxMaillon:
            self.Suivant[0].Position(Grille)


IndX = 0
IndY = 0
MaxX = 0
MinX = 0
MaxY = 0
MinY = 0

# On recupere les donnees initiales
with open(FichierInput) as file:
    Data = [f for f in file.read().strip().split("\n")]

# On recupere les informations de la grille
for l in Data:
    Direction,Cases = l.split(" ")
    if Direction == "L" :
        IndX = IndX - int(Cases)
        if IndX < MinX :
            MinX = IndX
    if Direction == "R":
        IndX = IndX + int(Cases)
        if IndX > MaxX:
            MaxX = IndX
    if Direction == "D":
        IndY = IndY + int(Cases)
        if IndY > MaxY :
            MaxY = IndY
    if Direction == "U":
        IndY = IndY - int(Cases)
        if IndY < MinY:
            MinY = IndY
PlageX = (MinX * (-1)) + MaxX + 2
PlageY = (MinY * (-1)) + MaxY + 2

print(f"{MinX} - {MaxX} / {MinY} - {MaxY}")

StartX = (MinX * (-1)) + 1
StartY = (MinY * (-1)) + 1
print(f"{StartX} - {StartY}")
# On cree la corde
H = Maillon(0, StartX, StartY)
for i in range(PlageY):
    Ligne=[]
    for j in range(PlageX):
        Ligne.append(0)
    H.Grille.append(Ligne)
H.Grille[StartY][StartX] = 1
Maillon_Actuel = H
for i in range(1,MaxMaillon+1,1):
    Maillon_Actuel.Add_Maillon(i)
    Maillon_Actuel = Maillon_Actuel.Suivant[0]
    for i in range(PlageY):
        Ligne = []
        for j in range(PlageX):
            Ligne.append(0)
        Maillon_Actuel.Grille.append(Ligne)
    Maillon_Actuel.Grille[StartY][StartX] = 1

Grille=[]
for i in range(PlageY):
    Ligne=[]
    for j in range(PlageX):
        Ligne.append(0)
    Grille.append(Ligne)

# On se deplace
for l in Data :
#    print(f"----------")
    Direction,Cases = l.split(" ")
#    print(f"{Direction} {Cases}")
    ClearTab(Grille,PlageX,PlageY)
    if Direction == "L":
        for i in range(int(Cases)):
            H.Horizontal(int(-1))
        H.Position(Grille)           
#        PTab(Grille)
    if Direction == "R":
        for i in range(int(Cases)):
            H.Horizontal(1)
        H.Position(Grille)
#        PTab(Grille)
    if Direction == "D":
        for i in range(int(Cases)):
            H.Vertical(1)
        H.Position(Grille)
#        PTab(Grille)

    if Direction == "U":
        for i in range(int(Cases)):
            H.Vertical(int(-1))
        H.Position(Grille)
#        PTab(Grille)


#print(f"---- FIN ------")
Resultat = 0
for i in range(PlageY):
    for j in range(PlageX):
        if Maillon_Actuel.Grille[i][j] != 0:
            Resultat = Resultat + 1

#Maillon_Actuel.PSTab()
print(Resultat)





