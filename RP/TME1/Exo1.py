from constraint import *

n = 9

# values = {'m', 'o', 'i', 't', 'l', 'u', 'e', 'n', 's'}

values = {'o', 'i', 'u','s'}
values2 = {'m', 't', 'l', 'e', 'n'}
values3 = {'r1', 'r2', 'r3'}

range1 = range(10)
range2 = range(1, 10)
range3 = range(2)

pb = Problem()
pb.addVariables(values, range1)
pb.addVariables(values2, range2)
pb.addVariables(values3, range3)

# constraints
# constraint 1 : S + 10 R1 = I + I + I + E
# constraint 2 : U + 10 R2 = O + O + U + L + R1
# constraint 3 : O + 10 R3 = M + T + L + L + R2
# constraint 4 : N = R3 + E


