from constraint import *
import json


with open('grille1.json') as json_file:
    data = json.load(json_file)

print(data)


pb = Problem()

pb.addVariables({'x11',  'x13',  'x15', 'x16', 'x19',
                 'x21',  'x24', 'x25', 'x27', 'x29',
                'x32', 'x34', 'x35', 'x36', 'x37', 'x38', 'x39',
                 'x41', 'x42',  'x44',  'x46', 'x47', 'x48',
                 'x51', 'x52', 'x53',  'x55',  'x57', 'x58', 'x59',
                  'x62', 'x63', 'x64',  'x66',  'x68', 'x69',
                 'x71', 'x72', 'x73', 'x74', 'x75', 'x76',  'x78',
                 'x81', 'x83',  'x85', 'x86', 'x87', 'x89',
                 'x91',   'x94', 'x95',  'x97',  'x99'}, range(1, 10))

pb.addVariables({'x23', 'x65', 'x77'}, range(1, 2))
pb.addVariables({'x28', 'x82'}, range(2, 3))
pb.addVariables({'x22', 'x54'}, range(3, 4))
pb.addVariables({'x93'}, range(4, 5))
pb.addVariables({'x26', 'x45', 'x61', 'x88', 'x92'}, range(5, 6))
pb.addVariables({'x18', 'x33', 'x49', 'x84'}, range(6, 7))
pb.addVariables({'x14', 'x43', 'x56', 'x67', 'x98'}, range(7, 8))
pb.addVariables({'x17', 'x31', 'x96'}, range(8, 9))
pb.addVariables({'x12', 'x79'}, range(9, 10))

# lignes
pb.addConstraint(AllDifferentConstraint(), ['x11', 'x12', 'x13', 'x14', 'x15', 'x16', 'x17', 'x18', 'x19'])
pb.addConstraint(AllDifferentConstraint(), ['x21', 'x22', 'x23', 'x24', 'x25', 'x26', 'x27', 'x28', 'x29'])
pb.addConstraint(AllDifferentConstraint(), ['x31', 'x32', 'x33', 'x34', 'x35', 'x36', 'x37', 'x38', 'x39'])
pb.addConstraint(AllDifferentConstraint(), ['x41', 'x42', 'x43', 'x44', 'x45', 'x46', 'x47', 'x48', 'x49'])
pb.addConstraint(AllDifferentConstraint(), ['x51', 'x52', 'x53', 'x54', 'x55', 'x56', 'x57', 'x58', 'x59'])
pb.addConstraint(AllDifferentConstraint(), ['x61', 'x62', 'x63', 'x64', 'x65', 'x66', 'x67', 'x68', 'x69'])
pb.addConstraint(AllDifferentConstraint(), ['x71', 'x72', 'x73', 'x74', 'x75', 'x76', 'x77', 'x78', 'x79'])
pb.addConstraint(AllDifferentConstraint(), ['x81', 'x82', 'x83', 'x84', 'x85', 'x86', 'x87', 'x88', 'x89'])
pb.addConstraint(AllDifferentConstraint(), ['x91', 'x92', 'x93', 'x94', 'x95', 'x96', 'x97', 'x98', 'x99'])

# colonnes
pb.addConstraint(AllDifferentConstraint(), ['x11', 'x21', 'x31', 'x41', 'x51', 'x61', 'x71', 'x81', 'x91'])
pb.addConstraint(AllDifferentConstraint(), ['x12', 'x22', 'x32', 'x42', 'x52', 'x62', 'x72', 'x82', 'x92'])
pb.addConstraint(AllDifferentConstraint(), ['x13', 'x23', 'x33', 'x43', 'x53', 'x63', 'x73', 'x83', 'x93'])
pb.addConstraint(AllDifferentConstraint(), ['x14', 'x24', 'x34', 'x44', 'x54', 'x64', 'x74', 'x84', 'x94'])
pb.addConstraint(AllDifferentConstraint(), ['x15', 'x25', 'x35', 'x45', 'x55', 'x65', 'x75', 'x85', 'x95'])
pb.addConstraint(AllDifferentConstraint(), ['x16', 'x26', 'x36', 'x46', 'x56', 'x66', 'x76', 'x86', 'x96'])
pb.addConstraint(AllDifferentConstraint(), ['x17', 'x27', 'x37', 'x47', 'x57', 'x67', 'x77', 'x87', 'x97'])
pb.addConstraint(AllDifferentConstraint(), ['x18', 'x28', 'x38', 'x48', 'x58', 'x68', 'x78', 'x88', 'x98'])
pb.addConstraint(AllDifferentConstraint(), ['x19', 'x29', 'x39', 'x49', 'x59', 'x69', 'x79', 'x89', 'x99'])

# carrés
pb.addConstraint(AllDifferentConstraint(), ['x11', 'x12', 'x13', 'x21', 'x22', 'x23', 'x31', 'x32', 'x33'])
pb.addConstraint(AllDifferentConstraint(), ['x14', 'x15', 'x16', 'x24', 'x25', 'x26', 'x34', 'x35', 'x36'])
pb.addConstraint(AllDifferentConstraint(), ['x17', 'x18', 'x19', 'x27', 'x28', 'x29', 'x37', 'x38', 'x39'])

pb.addConstraint(AllDifferentConstraint(), ['x41', 'x42', 'x43', 'x51', 'x52', 'x53', 'x61', 'x62', 'x63'])
pb.addConstraint(AllDifferentConstraint(), ['x44', 'x45', 'x46', 'x54', 'x55', 'x56', 'x64', 'x65', 'x66'])
pb.addConstraint(AllDifferentConstraint(), ['x47', 'x48', 'x49', 'x57', 'x58', 'x59', 'x67', 'x68', 'x69'])

pb.addConstraint(AllDifferentConstraint(), ['x71', 'x72', 'x73', 'x81', 'x82', 'x83', 'x91', 'x92', 'x93'])
pb.addConstraint(AllDifferentConstraint(), ['x74', 'x75', 'x76', 'x84', 'x85', 'x86', 'x94', 'x95', 'x96'])
pb.addConstraint(AllDifferentConstraint(), ['x77', 'x78', 'x79', 'x87', 'x88', 'x89', 'x97', 'x98', 'x99'])

solutions = pb.getSolutions()
print("Number of solutions : ", len(solutions))
print('solution 1 is : ', solutions[0])
print('solution 2 is : ', solutions[1])
print('solution 3 is : ', solutions[2])


# [2. 9. 5. 7. 4. 3. 8. 6. 1.]
# [4. 3. 1. 8. 6. 5. 9. 2. 7.]
# [8. 7. 6. 1. 9. 2. 3. 4. 5.]
# [3. 8. 7. 4. 5. 9. 2. 1. 6.]
# [6. 1. 2. 3. 8. 7. 5. 9. 4.]
# [5. 4. 9. 2. 1. 6. 7. 8. 3.]
# [7. 6. 8. 5. 2. 4. 1. 3. 9.]
# [9. 2. 3. 6. 7. 1. 4. 5. 8.]
# [1. 5. 4. 9. 3. 8. 6. 7. 2.]


# [2. 9. 5. 7. 4. 3. 8. 6. 1.]
# [4. 3. 1. 8. 6. 5. 9. 2. 7.]
# [8. 7. 6. 1. 9. 2. 3. 4. 5.]
# [3. 8. 7. 4. 5. 9. 2. 1. 6.]
# [6. 1. 2. 3. 8. 7. 5. 9. 4.]
# [5. 4. 9. 2. 1. 6. 7. 3. 8.]
# [7. 6. 3. 5. 2. 4. 1. 8. 9.]
# [9. 2. 8. 6. 7. 1. 4. 5. 3.]
# [1. 5. 4. 9. 3. 8. 6. 7. 2.]


# [2. 9. 5. 7. 4. 3. 8. 6. 1.]
# [4. 3. 1. 8. 6. 5. 9. 2. 7.]
# [8. 7. 6. 1. 9. 2. 5. 4. 3.]
# [3. 8. 7. 4. 5. 9. 2. 1. 6.]
# [6. 1. 2. 3. 8. 7. 4. 9. 5.]
# [5. 4. 9. 2. 1. 6. 7. 3. 8.]
# [7. 6. 3. 5. 2. 4. 1. 8. 9.]
# [9. 2. 8. 6. 7. 1. 3. 5. 4.]
# [1. 5. 4. 9. 3. 8. 6. 7. 2.]
