from constraint import *


# values = {'m', 'o', 'i', 't', 'l', 'u', 'e', 'n', 's', 'r1', 'r2', 'r3'}

# values = {'o', 'i', 'u', 's'}
# values2 = {'m', 't', 'l', 'e', 'n'}
# values3 = {'r1', 'r2', 'r3'}

range1 = range(10)
range2 = range(1, 10)
range3 = range(4)

pb = Problem()
pb.addVariables({'o', 'i', 'u', 's'}, range1)
pb.addVariables({'m', 't', 'l', 'e', 'n'}, range2)
pb.addVariables({'r1', 'r2', 'r3'}, range3)
pb.addConstraint(AllDifferentConstraint(), ['m', 'o', 'i', 't', 'l', 'u', 'e', 'n', 's'])

# constraints
# constraint 1 : S + 10 R1 = I + I + I + E
# constraint 2 : U + 10 R2 = O + O + U + L + R1
# constraint 3 : O + 10 R3 = M + T + L + L + R2
# constraint 4 : N = R3 + E

pb.addConstraint(lambda i, e, s, r1: (3 * i + e) == s + 10 * r1, ["i", "e", "s", "r1"])
pb.addConstraint(lambda u, o, l, r1, r2: (2 * o + u + l + r1) == u + 10 * r2, ["u", "o", "l", "r1", "r2"])
pb.addConstraint(lambda m, l, t, o, r2, r3: (m + t + 2*l + r2) == o + 10 * r3, ["m", "l", "t", "o", "r2", "r3"])
pb.addConstraint(lambda n, e, r3: e + r3 == n, ["n", "e", "r3"])


solutions = pb.getSolutions()
print("Nombre de solutions = ", len(solutions))
print(solutions[0])
