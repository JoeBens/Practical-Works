from constraint import *


# values = {'m', 'o', 'i', 't', 'l', 'u', 'e', 'n', 's', 'r1', 'r2', 'r3'}

# values = {'o', 'i', 'u', 's'}
# values2 = {'m', 't', 'l', 'e', 'n'}
# values3 = {'r1', 'r2', 'r3'}

range1 = range(10)
range2 = range(1, 10)
range3 = range(2)

values = range(12)
# 0 o 1 i 2 u 3 s 4 m 5 t 6 l 7 e 8 n 9 r1 10 r2 11 r3

pb = Problem()
pb.addVariable(values[0], range1)  # o
pb.addVariable(values[1], range1)  # i
pb.addVariable(values[2], range1)  # u
pb.addVariable(values[3], range1)  # s
pb.addVariable(values[4], range2)  # m
pb.addVariable(values[5], range2)  # t
pb.addVariable(values[6], range2)  # l
pb.addVariable(values[7], range2)  # e
pb.addVariable(values[8], range2)  # n
pb.addVariable(values[9], range3)  # r1
pb.addVariable(values[10], range3)  # r2
pb.addVariable(values[11], range3)  # r3

# constraints
# constraint 1 : S + 10 R1 = I + I + I + E
# constraint 2 : U + 10 R2 = O + O + U + L + R1
# constraint 3 : O + 10 R3 = M + T + L + L + R2
# constraint 4 : N = R3 + E

pb.addConstraint(ExactSumConstraint(values[3]), [3*values[1], values[7],  -10*values[9]])
pb.addConstraint(ExactSumConstraint(values[2]), [2*values[0], values[2], values[6], values[9], -10*values[10]])
pb.addConstraint(ExactSumConstraint(values[0]), [values[4], values[5], 2*values[6], values[10], -10*values[11]])
pb.addConstraint(ExactSumConstraint(values[8]), [values[11], values[7]])
solutions = pb.getSolutions()

print("Nombre de solutions = ", len(solutions))
print(solutions)




