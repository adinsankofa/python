'''
Exercício Python 091: Crie um programa onde 4 jogadores joguem um dado e
tenham resultados aleatórios. Guarde esses resultados em um dicionário em
Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor
tirou o maior número no dado.
'''

# VERSÃO GUANABARA:

from random import randint
from time import sleep
from operator import itemgetter
jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6),}
ranking = list()
print('Valores sorteados: ')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('-=' * 30)
print('== RANKING DOS JOGADORES ==')
for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} com {v[1]}.')
    sleep(1)




# VERSÃO BRUNO:

'''
import random

jogadores = dict()
jogo = list()
for i in range(1,5):
    aposta = 0
    aposta = random.randint(1,6)
    #jogadores['Jogador'] = i
    jogadores['Dado'] = aposta
    jogo.append(jogadores.copy())

for i in range(len(jogo)):
    print('Jogador', i+1, end=' tirou ')
    for v in jogo[i].values():
        print(v, end=" no dado.")
    print("\n")           
'''    
    
        



    
    
    
