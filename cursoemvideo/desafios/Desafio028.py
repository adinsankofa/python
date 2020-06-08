'''
Escreva um programa que faça o computador pensar em um número
inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi
o número escolhido pelo computador. O programa deve descrever
na tela se o usuário venceu ou perdeu.
'''
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5, tente advinhar...')
print('-=-' * 20)

from random import randint
from time import sleep
sorteado = randint(0,5)

jogador = int(input('Em que número eu pensei? '))

print('PROCESSANDO...')
sleep(2)

print('')
if jogador == sorteado:
    print('Pensei no {}, parabéns, você ganhou!'.format(sorteado))
else:
    print('Pensei no {}, perdeu playboy!'.format(sorteado))
