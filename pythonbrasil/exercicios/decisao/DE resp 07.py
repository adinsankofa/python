"""
Faça um Programa que leia três números e mostre o maior e o menor deles.
"""

maior = 0
menor = 1000

for i in range(1,4):
    num = int(input("Digite o %iº número: "%(i)))

    if num > maior:
        maior = num

    if num < menor:
        menor = num

print("")

print("Maior número: %i " %(maior))
print("Menor número: %i " %(menor))

    
