'''
Exercício Python 045: Crie um programa que faça o computador
jogar Jokenpô com você.
'''

from time import sleep
from random import randint

print('Suas opções:')
print('[ 0 ] PEDRA')
print('[ 1 ] PAPEL')
print('[ 2 ] TESOURA')

jogada = int(input('Qual é a sua jogada? '))

print('')

itens = ('Pedra', 'Papel', 'Tesoura')

sorteado = randint(0,3)

resultado = ('EMPATE', 'JOGADOR VENCE', 'COMPUTADOR VENCE')

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')

print('')

print('-=' * 15)

print('Computador jogou {}.'.format(itens[sorteado]))
print('Jogador jogou {}.'.format(itens[jogada]))
print('-=' * 15)

print('')
if sorteado == 0:
    if jogada == 0:
        print('EMPATE')
    elif jogada == 1:
        print('JOGADOR VENCE')
    elif jogada == 2:
        print('COMPUTADOR VENCE')
    else:
        print('JOGADA INVÁLIDA')
elif sorteado == 1:
    if jogada == 0:
        print('COMPUTADOR VENCE')
    elif jogada == 1:
        print('EMPATE')
    elif jogada == 2:
        print('JOGADOR VENCE')
    else:
        print('JOGADA INVÁLIDA')
elif sorteado == 2:
    if jogada == 0:
        print('JOGADOR VENCE')
    elif jogada == 1:
        print('COMPUTADOR VENCE')
    elif jogada == 2:
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA') 

print('')




