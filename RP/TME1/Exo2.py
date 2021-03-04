from constraint import *


# BINOME : MOUNIB BENIMAM et YOUCEF BENSLIMANE

pb = Problem()

pb.addVariables(["x", "y"], range(10))
pb.addVariable("number", range(100000))

pb.addConstraint(lambda a, b, num: (173 * num) == (2020 * 1000 + a * 100 + 20 + b), ["x", "y", "number"])

solutions = pb.getSolutions()

print(solutions)

# [{'x': 1, 'y': 1, 'number': 11677}]
