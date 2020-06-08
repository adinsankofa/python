'''
Faça um programa que leia 5 números e informe o maior número.
'''

maior = 0

for i in range(1,6):
    num = int(input("Digite o %iº número: "%(i)))

    if num > maior:
        maior = num

print("")
print("O maior número digitado foi:", maior)
print("")
