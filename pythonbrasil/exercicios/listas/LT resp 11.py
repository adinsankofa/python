"""
Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.
"""

elementos = 10
A = []
B = []
C = []
D = []

for i in range(1,elementos + 1):
    
    numA = int(input("Digite %iº de A: "%(i)))
    A.append(numA)

    numB = int(input("Digite %iº de B: "%(i)))
    B.append(numB)

    numC = int(input("Digite %iº de C: "%(i)))
    C.append(numC)

    D = A + B + C

print("")
print("A: ", A)
print("B: ", B)
print("C: ", C)
print("")
print("A + B: ", D)
print("")

