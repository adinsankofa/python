'''
Faça um programa que, dado um conjunto de N números, determine o
menor valor, o maior valor e a soma dos valores.
'''


elementos = 5

n = int(input("Digite o 1º número: "))
menor = n
maior = n
soma = 0

for i in range(2, elementos+1):
    n = int(input("Digite o %iº número: "%(i)))

    if n > maior:
        maior = n

    if n < menor:
        menor = n

    soma += n

print("")
print("MAIOR: ", maior)
print("MENOR: ", menor)
print("Soma (MAIOR + MENOR): ", maior + menor)
print("Soma dos valores: ", soma)
print("")
