#!/usr/bin/env python3

#On recupere les donnees initiales
with open('Input.7') as file:
    Shell = [i for i in file.read().strip().split("\n")[1:]]


class Fichier:
    """Classe pour la gestion des fichiers"""
    Type = "File"
    def __init__(self,Nom):
        self.Nom = Nom
        self.Taille = 0

class Repertoire:
    """Classe pour la gestion des repertoires"""
    Type = "Rep"

    def __init__(self,Nom):
        self.Nom = Nom
        self.Taille = 0
        self.Parent = []
        self.Liste_Fichiers = []
        self.List_Ind = 0
        self.TailleProche = 0
        self.Min = 30000000
    
    def Add_File(self,FileName,Taille):
        Filetmp = Fichier(FileName)
        Filetmp.Taille = int(Taille)
        self.Liste_Fichiers.append(Filetmp)
        self.List_Ind += 1

    def Add_Repertoire(self,DirName):
        Dirtmp = Repertoire(DirName)
        Dirtmp.Parent.append(self)
        self.Liste_Fichiers.append(Dirtmp)
        self.List_Ind += 1

    def Calcul_Taille(self):
        Somme = 0
        ResultTmp = 0
        for i in range(self.List_Ind):
            ObjTmp = self.Liste_Fichiers[i]
            if ObjTmp.Type == "File":
                Somme += ObjTmp.Taille
            elif ObjTmp.Type == "Rep":
                ObjTmp.Calcul_Taille()
                Somme += ObjTmp.Taille
        self.Taille = Somme

    def Recherche_Min(self,Taille):
        self.TailleProche = self.Taille
        if self.Taille < Taille:
            self.Min = 0
        else :
            self.Min = self.Taille - Taille

        for i in range(self.List_Ind):
            ObjTmp = self.Liste_Fichiers[i]
            if ObjTmp.Type == "Rep":
                ObjTmp.Recherche_Min(Taille)
                if ObjTmp.Min < self.Min and ObjTmp.Min > 0 :
                    self.TailleProche = ObjTmp.TailleProche
                    self.Min = ObjTmp.Min
                elif self.Min == 0 :
                    self.TailleProche = ObjTmp.TailleProche
                    self.Min = ObjTmp.Min


TailleDisque = 70000000
TailleNecessaire = 30000000

Arborescence = Repertoire("/")
Repertoire_Actuel = Arborescence

for Commandes in Shell:
    if Commandes[0:4] == "$ ls":
        pass
    if Commandes[0:4] == "$ cd":
        Nom = Commandes[5:]
        if Nom == "..":
            Repertoire_Actuel = Repertoire_Actuel.Parent[0]
        else:
            Repertoire_Actuel.Add_Repertoire(Commandes[5:])
            Repertoire_Actuel = Repertoire_Actuel.Liste_Fichiers[Repertoire_Actuel.List_Ind -1]
    if Commandes[0:3] == "dir" :
        pass
    if Commandes[0].isnumeric() :
        Taille_Str,Nom = Commandes.split(' ')
        Taille=int(Taille_Str)
        Repertoire_Actuel.Add_File(Nom,Taille)

Arborescence.Calcul_Taille()
print(f"Taille : {Arborescence.Taille}")
TailleActuelle = Arborescence.Taille 
TailleNeed = TailleActuelle - (TailleDisque - TailleNecessaire)
print(f"Besoin d effacer au min {TailleNeed}")


Arborescence.Recherche_Min(TailleNeed)

print(Arborescence.TailleProche)

