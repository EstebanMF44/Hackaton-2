import numpy as np
import random as rd 
from collections import deque

goal = np.array([[1,2,3], [4,5,6], [7,8,0]])
graph = {}

def generer_voisin(tuple):
    l = []
    tableau = hash_ar(tuple)
    tableau1 = tableau.copy()  # un cran au dessus
    tableau2 = tableau.copy()  # un cran en dessous
    tableau3 = tableau.copy()  # un cran à gauche
    tableau4 = tableau.copy()  # un cran à droite
    position = [0, 0]
    for i in range(3):  # on cherche la position du 0
        for j in range(3):
            if tableau[i][j] == 0:
                position = [i, j]
    if (position[0] - 1) in [0, 1, 2]:
        tableau1[position[0]][position[1]] = tableau1[position[0] - 1][
            position[1]
        ]  # le zéro est remplacé
        tableau1[position[0] - 1][position[1]] = 0  # le zéro remplace
        l.append(tableau1)
    if (position[0] + 1) in [0, 1, 2]:
        tableau2[position[0]][position[1]] = tableau1[position[0] + 1][
            position[1]
        ]  # le zéro est remplacé
        tableau2[position[0] + 1][position[1]] = 0  # le zéro remplace
        l.append(tableau2)
    if (position[1] - 1) in [0, 1, 2]:
        tableau3[position[0]][position[1]] = tableau1[position[0]][
            position[1] - 1
        ]  # le zéro est remplacé
        tableau3[position[0]][position[1] - 1] = 0  # le zéro remplace
        l.append(tableau3)
    if (position[0] + 1) in [0, 1, 2]:
        tableau4[position[0]][position[1]] = tableau1[position[0]][
            position[1] + 1
        ]  # le zéro est remplacé
        tableau4[position[0]][position[1] + 1] = 0  # le zéro remplace
        l.append(tableau4)
    return l

def ar_hash(L):
    return tuple(map(tuple, L))

def hash_ar(L):
    return [list(row) for row in L]

def creation_graph_largeur(initial):
    # renvoie la liste des sommets atteignables depuis sommet
    graphe = {}  
    file = deque([initial]) 
    visités = set()  
    
    while file:
        etat_courant = ar_hash(file.popleft()) 

        if etat_courant in visités:
            continue

        visités.add(etat_courant)  
        voisins = generer_voisin(etat_courant)  

        graphe[ar_hash(etat_courant)] = voisins  

        for voisin in voisins:
            if ar_hash(voisin) not in visités:
                file.append(voisin)  
    
    return graphe 


initial = np.array([[1, 2, 3], [4, 5, 6], [7, 0, 8]])
print(creation_graph_largeur(initial))