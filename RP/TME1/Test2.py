from constraint import *

# Dimension du problème
n = 3

# Création du problème
pb = Problem()

# Création d’une liste python x représentant les n^2 nombres à placer dans la grille
x = range(1, n**2 + 1)

# Ajout de x dans le problème. Chaque  ́element de x a pour domaine {1, ..., n**2 + 1}
pb.addVariables(x, x)

# Ajout de la contrainte AllDiff
pb.addConstraint(AllDifferentConstraint())

# Variable contenant la somme de chaque ligne/colonne/diagonale
s = n * (n**2 + 1) / 2

# Ajout des contraintes du carré magique
for k in range(n):
    # ligne k
    pb.addConstraint(ExactSumConstraint(s), [x[k*n+i] for i in range(n)])
    # colonne k
    pb.addConstraint(ExactSumConstraint(s), [x[k+n*i] for i in range(n)])
    # première diagonale
    pb.addConstraint(ExactSumConstraint(s), [x[n*i+i] for i in range(n)])
    # deuxième diagonale
    pb.addConstraint(ExactSumConstraint(s), [x[(n-1)*i] for i in range(1, n+1)])

solutions = pb.getSolutions()

print("Nombre de solutions = ", len(solutions))
print(solutions)