from random import choice
import os #pour les chemins de fichiers
import pickle #le module pickle permet de sauvegarder dans un fichier, au format binaire,  n'importe quel objet Python.

from data import *

def recup_score():
    if os.path.exists(fichier): #renvoie True si le fichier ou directory existe. Si c'est un lien symbolique qui pointe vers un fichier qui n'existe pas, renvoie False.
        f = open(fichier, "rb")
        mon_depickler = pickle.Unpickler(f)
        scores = mon_depickler.load()
        #f = open("fichier.csv", "r")
        #scores = f.read()
        #f.close()
    else:
        scores = {}
    return scores

def enregistrer_scores(scores):
    f = open(fichier, "wb")
    mon_pickler = pickle.Pickler(f)
    mon_pickler.dump(scores)
    f.close()
    #f = open("fichier.csv", "w")
    #f.write(scores)
    #f.close()

def afficher(a, sep=' '): # on enléve les guillemets et les virgules et on mettra espace à la place
            chaine = sep.join(a) #on colle les éléments ensemble
            print(chaine)
            
def lettre():
    continuer = True
    while continuer:
        mon_lettre = input("Tapez une lettre: ")
        mon_lettre = mon_lettre.lower()
        
        if mon_lettre.isalpha() == False or len(mon_lettre) != 1:
            print("Ce n'est pas une lettre d'alphabet ou votre lettre est supérieur à 1 lettre.")
            continue
        else:
            continuer = False
            return mon_lettre
def pseudo():
        continuer = True
        while continuer:
            mon_pseudo = input('Entrez votre nom (min. 4 character): ')
            mon_pseudo = mon_pseudo.capitalize()
            if mon_pseudo.isalnum() == False or len(mon_pseudo) < 4:
                print('Votre nom doit etre composer des lettres et des chifres et doit avoir au moins 4 character.')
                continue
            else:
                continuer = False
                return mon_pseudo
def quitter():
        c = True
        while c:
            quitter = input("Veux tu encore jouer? o/n: ")
            if quitter == 'N' or quitter == 'n':
                continuer_partie = False
                c = False
            elif quitter == 'O' or quitter == 'o':  
                continuer_partie = True
                c = False
            else:
                print("il faut mettre O/N!")
                continue
        return continuer_partie
