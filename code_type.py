# 1. Conversions Matrice <-> Dictionnaire d'adjacence
from collections import deque

def matrice_vers_dict(matrice, sommets):
     graphe = {s: [] for s in sommets}
     for i in range(len(sommets)):
         for j in range(len(sommets)):
             if matrice[i][j] != 0:
                 graphe[sommets[i]].append(sommets[j])
     return graphe

# 2. Parcours en largeur (BFS) avec une file FIFO

def bfs(graphe, depart):
     visites = [depart]
     file = deque([depart])
     while file:
         sommet = file.popleft()
         for voisin in graphe[sommet]:
             if voisin not in visites:
                 visites.append(voisin)
                 file.append(voisin)
     return visites

# 3. Parcours en profondeur (DFS) récursif et itératif (pile LIFO)

def dfs_recursif(graphe, sommet, visites=None):
     if visites is None:
         visites = []
     visites.append(sommet)
     for voisin in graphe[sommet]:
         if voisin not in visites:
             dfs_recursif(graphe, voisin, visites)
     return visites

def dfs_iteratif(graphe, depart):
     visites, pile = [], [depart]
     while pile:
         sommet = pile.pop()
         if sommet not in visites:
             visites.append(sommet)
             for voisin in reversed(graphe[sommet]):
                 if voisin not in visites:
                     pile.append(voisin)
     return visites

# 4. Détection de cycle dans un graphe NON ORIENTÉ

def contient_cycle(graphe, sommet, visites=None, parent=None):
     if visites is None:
         visites = []
     visites.append(sommet)
     for voisin in graphe[sommet]:
         if voisin not in visites:
             if contient_cycle(graphe, voisin, visites, sommet):
                 return True
         elif voisin != parent:
             return True
     return False

# 5. Plus court chemin en nombre d'arêtes (BFS + reconstruction)

def plus_court_chemin(graphe, depart, arrivee):
     parents = {depart: None}
     file = deque([depart])
     while file:
         sommet = file.popleft()
         if sommet == arrivee:
             chemin = []
             courant = arrivee
             while courant is not None:
                 chemin.append(courant)
                 courant = parents[courant]
             return chemin[::-1]
         for voisin in graphe[sommet]:
             if voisin not in parents:
                 parents[voisin] = sommet
                 file.append(voisin)
     return None


