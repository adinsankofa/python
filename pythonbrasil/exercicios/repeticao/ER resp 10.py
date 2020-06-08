'''
Faça um programa que receba dois números inteiros e gere os
números inteiros que estão no intervalo compreendido por eles.
'''

# Utilizando o FOR (imprimindo na vertical)

numA = int(input("Digite o número A: "))
numB = int(input("Digite o número B: "))

print("")

if numB > numA:
    for i in range(numA+1, numB):
        print(i)

if numA > numB:
    for i in range(numB+1, numA):
        print(i)

print("")





# Utilizando o WHILE (imprimindo na horizontal)

numA = int(input("Digite o número A: "))
numB = int(input("Digite o número B: "))

print("")

numC = numA+1
numD = numB+1

if numA < numB:
    while numA <= numB:
        print(numC, end = " ")
        numC += 1

        if numC == numB:
            break
print("")

if numB < numA:
    while numB < numA:
        print(numD, end = " ")
        numD += 1

        if numD == numA:
            break
print("")
 


 

    
