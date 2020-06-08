'''
Exercício Python 085: Crie um programa onde o usuário possa digitar sete
valores numéricos e cadastre-os em uma lista única que mantenha separados
os valores pares e ímpares. No final, mostre os valores pares e ímpares em
ordem crescente.
'''


## VERSÃO GUANABARA:
num = [[],[]]
valor = 0
for c in range(1,8):
    valor = int(input(f'Digite o {c}º valor: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
print('-=' * 30)
num[0].sort()
num[1].sort()
print(f'Os valores pares digitados foram: {num[0]}')
print(f'Os valores pares digitados foram: {num[1]}')




## VERSÃO BRUNO:
lista = list()
pares = list()
impares = list()
for i in range(1,8):
    lista.append(int(input(f"Digite o {i}º valor: ")))
for i in lista:
    if i % 2 == 0:
        pares.append(i)
    else:
        impares.append(i)
print('-=' * 30)
pares.sort()
print(f"Os valores pares digitados foram: {pares}")
impares.sort()
print(f"Os valores ímpares digitados foram: {impares}")

            

