"""
Faça um Programa que leia três números e mostre o maior deles.
"""

maior = 0

for i in range(1,4):
    num = int(input("Digite o %iº número: " %(i)))

    if num > maior:
        maior = num

print("")
print("Maior número: %i " %(maior))
