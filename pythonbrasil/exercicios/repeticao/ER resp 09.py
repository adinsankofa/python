'''
Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50.
'''

# Imprimir na VERTICAL

for i in range(1,51):
    if i % 2 == 1:
        print(i)


# Imprimir na HORIZONTAL

for i in range(1,51):
    if i % 2 == 1:
        print(i, end = " ")

