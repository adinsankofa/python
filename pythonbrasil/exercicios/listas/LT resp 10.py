"""
Faça um Programa que leia dois vetores com 10 elementos cada.
Gere um terceiro vetor de 20 elementos, cujos valores deverão
ser compostos pelos elementos intercalados dos dois outros vetores.
"""

elementos = 10
A = []
B = []
C = []

for i in range(1,elementos + 1):
    
    numA = int(input("Digite %iº de A: "%(i)))
    A.append(numA)

    numB = int(input("Digite %iº de B: "%(i)))
    B.append(numB)

    C = A + B

print("")
print("A: ", A)
print("B: ", B)
print("")
print("A + B: ", C)
print("")

