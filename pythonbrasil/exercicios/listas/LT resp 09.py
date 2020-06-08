'''
"Faça um Programa que leia um vetor A com 10 números inteiros,
calcule e mostre a soma dos quadrados dos elementos do vetor."
'''


numeros = 10
A = []
soma = 0
N = []

for i in range(1, numeros+1):
    num = int(input("Digite o %iº número: "%(i)))

    quad = num ** 2

    soma += quad

    N.append(num)
      
    A.append(quad)

print ("")
for i in range(numeros):
    print("Quadrado do elemento nº ", (i+1), "(", N[i], "x", N[i],")", " = ", A[i])

print("")
print("Soma dos Quadrados", A, "=", soma)
    
    
    
