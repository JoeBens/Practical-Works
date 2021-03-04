from constraint import *

n = 9

# values = {'m', 'o', 'i', 't', 'l', 'u', 'e', 'n', 's', 'r1', 'r2', 'r3'}

# values = {'o', 'i', 'u', 's'}
# values2 = {'m', 't', 'l', 'e', 'n'}
# values3 = {'r1', 'r2', 'r3'}

range1 = range(10)
range2 = range(1, 10)
range3 = range(2)

pb = Problem()
pb.addVariables({'o', 'i', 'u', 's'}, range1)
pb.addVariables({'m', 't', 'l', 'e', 'n'}, range2)
pb.addVariables({'r1', 'r2', 'r3'}, range3)

# constraints
# constraint 1 : S + 10 R1 = I + I + I + E
# constraint 2 : U + 10 R2 = O + O + U + L + R1
# constraint 3 : O + 10 R3 = M + T + L + L + R2
# constraint 4 : N = R3 + E

pb.addConstraint(ExactSumConstraint(['s', 'r1', 'r1', 'r1', 'r1', 'r1', 'r1', 'r1', 'r1', 'r1', 'r1']), ['i', 'i', 'i','e'])
pb.addConstraint(ExactSumConstraint(['u', 'r2', 'r2', 'r2', 'r2', 'r2', 'r2', 'r2', 'r2', 'r2', 'r2']), ['o', 'o', 'u', 'l', 'r1'])
pb.addConstraint(ExactSumConstraint(['o', 'r3', 'r3', 'r3', 'r3', 'r3', 'r3', 'r3', 'r3', 'r3', 'r3']), ['m', 't', 'l', 'l', 'r2'])
pb.addConstraint(ExactSumConstraint(['n']), ['r3', 'e'])

solutions = pb.getSolutions()

print("Nombre de solutions = ", len(solutions))
print(solutions)




