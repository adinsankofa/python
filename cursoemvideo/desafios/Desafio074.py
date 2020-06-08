'''
Exercício Python 074: Crie um programa que vai gerar cinco números aleatórios e
colocar em uma tupla. Depois disso, mostre a listagem de números gerados e
também indique o menor e o maior valor que estão na tupla.
'''


## VERSÃO GUANABARA:

from random import randint
numeros = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))
print("Os valores sorteados foram: ", end="")
for n in numeros:
    print(f'{n} ', end='')
print(f"\nO maior valor sorteador foi {max(numeros)}")
print(f"O menor valor sorteador foi {min(numeros)}")




## VERSÃO BRUNO:
import random
lista_sorteados = ()
for i in range(5):
    num_sorteado = random.randrange(10)
    lista_sorteados = lista_sorteados + (num_sorteado,)

print("Os valores sorteados foram: ", end="")
for i in lista_sorteados:
    print(i, end=" ")

print(f"\nO maior valor sorteador foi {max(lista_sorteados)}")
print(f"O menor valor sorteador foi {min(lista_sorteados)}")
