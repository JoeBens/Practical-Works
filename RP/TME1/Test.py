from constraint import *

# Dimension du problème
n = 8
# Création du problème
pb = Problem()
# Création d’une liste python cols de dimension n(num ́ero de colonnes associé aux tours (une tour par ligne))
cols = range(n)
# Ajout de cols dans le problème. Chaque  ́elément de cols a pour domaine {1, ..., n}
pb.addVariables(cols, range(n))
# Ajout de la contrainte AllDiff
pb.addConstraint(AllDifferentConstraint())
# Récupération d’une solution
s = pb.getSolution()
# Récupération de l’ensemble des solutions possibles
s = pb.getSolutions()

print("Nombre de solutions = ", len(s))
#print(s)