'''
Faça um programa que simule um lançamento de dados. Lance o dado 100 vezes e
armazene os resultados em um vetor . Depois, mostre quantas vezes cada valor
foi conseguido. Dica: use um vetor de contadores(1-6) e uma função para gerar
numeros aleatórios, simulando os lançamentos dos dados.
'''

import random

lancamentos = []
lanc = []
frequencia = []
print(' {}'.format('_'*26))
for i in range(1,100):
    lancamentos.append(random.randint(1,100))

lanc = set(lancamentos)

for i in lanc:
    frequencia.append(i)

print('| NÚMERO   |', '\tFREQUÊNCIA |')
print('| {} |'.format('-'*24))
for i in frequencia:
    print('| {:3} \t   -\t {:5}     |'.format(i,lancamentos.count(i)))
print('|{}|'.format('_'*26))
