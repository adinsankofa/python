'''
Faça um programa que calcule o fatorial de
um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120
'''


## Fatorial com estrutura WHILE

i = 1
fat = 1

n = int(input("Digite o fatorial que você quer: "))

while i <= n:
    fat = fat * i
    i += 1

print("")
print("Fatorial de %s! "%n)
print(str(n), end = "! = ") ## <= aqui se imprime o fatorial em forma de string
for i in range(n, 1, -1):
    print(i, end = " x ")
    if i == 2:
        print("1 =", fat)

print("")




## Fatorial com estrutura FOR
fat = 1

n = int(input("Digite o fatorial que você quer: "))

for i in range(n, 1, -1):
    fat *= i

print("")
print("Fatorial de %s! "%n)
print(str(n), end = "! = ") ## <= aqui se imprime o fatorial em forma de string
for i in range(n, 1, -1):
    print(i, end = " x ")
    if i == 2:
        print("1 =", fat)

print("")
