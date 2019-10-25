from data import *
from functions import *

scores = recup_score()    
mon_pseudo = pseudo()

if mon_pseudo not in scores.keys():
    score = 0
    scores[mon_pseudo] = score
else:
    score = scores[mon_pseudo]
        
print("Salut {0} , ton score jusqu'à maintenaint est {1} point. J'espère, que tu es prêt, car on commence jouer!".format(mon_pseudo, score))


continuer_partie = True
while continuer_partie:
    
    mot_d_ordi = choice(mots)
    mot_d_ordi = list(mot_d_ordi)
    a = len(mot_d_ordi)* "*"
    a = list(a)
    print('mot à trouver (encore 9 chance)')
    afficher(a)
    nb_coup = 9
    continuer = True

    while continuer:
        point = 0
        if nb_coup > 0:
       
            mon_lettre = lettre()
            b = 0
        
            for i,j in enumerate(mot_d_ordi): # Un besoin assez courant quand on manipule une liste ou tout autre objet itérable est de récupérer en même temps l'élément et son indice à chaque itération.
          
                if j == mon_lettre:
                    a[i] = j

                elif j != mon_lettre:
                    b += 1
                   
            if b == len(mot_d_ordi):
                print('cette lettre ne se trouve pas dans le mot...')
                
            elif a == mot_d_ordi:
                print('Bravo tu as trouvé le mot!')
                #nb_coup - 1
                point = 2
                score += point - 1 
                break
            
            else:
                print('bien joué')
                nb_coup += 1
           
            nb_coup = nb_coup - 1
            print('Tu as encore {} chance'.format(nb_coup))      
            afficher(a)
            
        else:
            print("Tu es pendu!")
            point = 1
            score += point - 1
    
        if point == 0:
            continuer = True
        else:
            continuer = False
    print("mon mot est  "), afficher(mot_d_ordi)   
    scores[mon_pseudo] = score
    continuer_partie = quitter()
    

enregistrer_scores(scores)
print("Tu as {} point(s) pour l'instant.".format(score))
print(scores)
