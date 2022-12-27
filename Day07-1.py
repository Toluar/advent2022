#!/usr/bin/env python3

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
        self.Resultat = 0
    
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
#        print(f"Calcul de la taille du repertoire {self.Nom}")
        for i in range(self.List_Ind):
            ObjTmp = self.Liste_Fichiers[i]
            if ObjTmp.Type == "File":
                Somme += ObjTmp.Taille
            elif ObjTmp.Type == "Rep":
                ObjTmp.Calcul_Taille()
                Somme += ObjTmp.Taille
                if ObjTmp.Taille < 100000:
                    ResultTmp += ObjTmp.Taille + ObjTmp.Resultat
                else:
                    ResultTmp += ObjTmp.Resultat
#                    print(f"{self.Nom} : Resultat = {self.Resultat}")
        self.Taille = Somme
        self.Resultat = ResultTmp
#        print(f"{self.Nom} : Taille {self.Taille}")

        

#On recupere les donnees initiales
with open('Input.7') as file:
    Shell = [i for i in file.read().strip().split("\n")[1:]]

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
print(f"Resultat : {Arborescence.Resultat}")



