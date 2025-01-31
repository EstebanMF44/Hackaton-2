import numpy as np
import random as rd
from collections import deque

graph = {}


def generer_voisin(tup):
    LLL = []
    tableau = tuple_to_array(tup)
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
        LLL.append(tableau1)
    if (position[0] + 1) in [0, 1, 2]:
        tableau2[position[0]][position[1]] = tableau1[position[0] + 1][
            position[1]
        ]  # le zéro est remplacé
        tableau2[position[0] + 1][position[1]] = 0  # le zéro remplace
        LLL.append(tableau2)
    if (position[1] - 1) in [0, 1, 2]:
        tableau3[position[0]][position[1]] = tableau1[position[0]][
            position[1] - 1
        ]  # le zéro est remplacé
        tableau3[position[0]][position[1] - 1] = 0  # le zéro remplace
        LLL.append(tableau3)
    if (position[0] + 1) in [0, 1, 2]:
        tableau4[position[0]][position[1]] = tableau1[position[0]][
            position[1] + 1
        ]  # le zéro est remplacé
        tableau4[position[0]][position[1] + 1] = 0  # le zéro remplace
        LLL.append(tableau4)
    return LLL


def array_to_tuple(L):
    return tuple(map(tuple, L))


def tuple_to_array(L):
    return [list(row) for row in L]


def creation_graph_largeur(initial):
    # renvoie la liste des sommets atteignables depuis sommet
    graphe = {}
    file = deque([initial])
    visités = set()

    while file:
        etat_courant = array_to_tuple(file.popleft())

        if etat_courant in visités:
            continue

        visités.add(etat_courant)
        voisins = generer_voisin(etat_courant)

        graphe[array_to_tuple(etat_courant)] = voisins

        for voisin in voisins:
            if array_to_tuple(voisin) not in visités:
                file.append(voisin)

    return graphe


def bfs_find_goal(dico, goal):
    goal_tuple = array_to_tuple(goal)
    for start in dico:  # On ne sait pas où commence le parcours
        queue = deque([(start, [start])])  # File d'attente avec chemin
        visited = set()

        while queue:
            current, path = queue.popleft()
            visited.add(current)

            for neighbor in dico.get(current, []):
                neighbor_tuple = array_to_tuple(neighbor)
                if neighbor_tuple == goal_tuple:  # Si on trouve goal
                    return path + [neighbor_tuple]
                if neighbor_tuple not in visited:
                    queue.append((neighbor_tuple, path + [neighbor_tuple]))
                    visited.add(neighbor_tuple)

    return None  # Si goal n'est pas trouvé


def print_path(path):
    """Affiche le chemin de manière lisible."""
    if path:
        print("Chemin trouvé :")
        for step in path:
            print(tuple_to_array(step))
            print("↓")
    else:
        print("Aucun chemin trouvé.")


initial = np.array([[1, 2, 3], [4, 5, 6], [7, 0, 8]])
print(tuple_to_array(array_to_tuple(initial)))
# print(generer_voisin(tuple(initial)))
goal = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]])
dico = creation_graph_largeur(initial)
# print(dico)
path = bfs_find_goal(dico, goal)
# print_path(path)
