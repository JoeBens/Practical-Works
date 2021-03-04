from constraint import *
import numpy as np
# a 100 dim 20 qs 20 val 8
# b 45 dim 7 qs 16 val 6.8
# c 10 dim 3 qs 9 val 4
# d 25 dim 4.5 qs 7 val 3

variables = {'a', 'b', 'c', 'd'}

pb = Problem()
pb.addVariable('a', range(30))
pb.addVariable('b', range(45))
pb.addVariable('c', range(75))
pb.addVariable('d', range(100))

pb.addConstraint(lambda a, b, c, d: a*100 + b*45 + c*10 + d*25 <= 3000, ['a', 'b', 'c', 'd'])
pb.addConstraint(lambda a, b, c, d: a*10 + b*7 + c*3 + d*4.5 <= 1000, ['a', 'b', 'c', 'd'])
pb.addConstraint(lambda a, b, c, d: a*8 + b*6.8 + c*4 + d*3 <= 300, ['a', 'b', 'c', 'd'])

solutions = pb.getSolutions()
print('Nombre de solutions : ', len(solutions))
solu = np.array((solutions))

maxSugar = 0
best_solu = solutions[0]
for s in solutions:
    sugar_q = s['a'] * 20 + s['b'] * 16 + s['c'] * 9 + s['d'] * 7
    if sugar_q >= maxSugar:
        maxSugar = sugar_q
        best_solu = s

print('Maximum sugar quantity : ', maxSugar)
print('Best solution : ', best_solu)

# Résultats
# Nombre de solutions :  588571
# Maximum sugar quantity :  731
# Best solution :  {'a': 28, 'b': 0, 'c': 19, 'd': 0}
