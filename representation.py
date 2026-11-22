#Matrice liste des listes

m = [
    [0,1,1,0],
    [1,0,0,1],
    [1,0,0,1],
    [0,1,1,0]
]

#test lien a b M[0][1]

#dictionnaire d'adjacence

g = {
    "A" : ["B" , "C"],
    "B" : ["A" , "D"],
    "C" : ["A" , "D"],
    "D" : ["B" , "C"]
}