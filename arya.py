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


print(remplissage_tableau())
