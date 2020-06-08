'''
Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa
que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.
'''

import random

aluno1 = str(input('Primeiro aluno: '))
aluno2 = str(input('Segundo aluno: '))
aluno3 = str(input('Terceiro aluno: '))
aluno4 = str(input('Quarto aluno: '))

lista = [aluno1,aluno2,aluno3,aluno4]

escolhido = random.choice(lista)

print('O aluno escolhido foi {}.'. format(escolhido))


