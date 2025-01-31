# DOC d'Arya
# Puzzle 8 : 'taquin'
import numpy as np
import random as rd

goal = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]])

# Remplissage du tableau initial


def remplissage_tableau():
    aléatoire = rd.sample([1, 2, 3, 4, 5, 6, 7, 8, 0], 9)
    initial = np.zeros((3, 3))
    initial[0][0] = aléatoire[0]
    initial[0][1] = aléatoire[1]
    initial[0][2] = aléatoire[2]
    initial[1][0] = aléatoire[3]
    initial[1][1] = aléatoire[4]
    initial[1][2] = aléatoire[5]
    initial[2][0] = aléatoire[6]
    initial[2][1] = aléatoire[7]
    initial[2][2] = aléatoire[8]
    return initial


# test : print(remplissage_tableau())


# Solveur
# On renvoie les tableaux atteignables à partir d'une position après 1 seul déplacement du 0
def atteignable(tableau):
    l = []
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


# un exemple : print(atteignable(np.array([[2, 3, 4], [5, 0, 1], [8, 6, 7]])))
