from constraint import *

# BINOME : MOUNIB BENIMAM et YOUCEF BENSLIMANE

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

nous_max_value = 0
best_solu = solutions[0]

for s in solutions:
    res = 1*(3*s['i'] + s['e'] - 10*s['r1']) + 10 * (2 * s['o'] + s['u'] + s['l'] + s['r1'] - 10 * s['r2']) + 100 * (s['m'] + s['t'] + 2*s['l'] + s['r2'] - 10 * s['r3']) + 1000 * (s['e']+s['r3'])
    if res >= nous_max_value:
        nous_max_value = res
        best_solu = s

print('Maximum Nous Value : ', nous_max_value)
print('Best solution : ', best_solu)

# Nombre de solutions =  160
# Maximum Nous Value :  9723
# Best solution :  {'e': 8, 'l': 4, 'o': 7, 'r1': 2, 'r2': 2, 'r3': 1, 'n': 9, 'm': 1, 't': 6, 'i': 5, 's': 3, 'u': 2}
