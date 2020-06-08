'''
Faça um programa que jogue par ou ímpar com o computador.
O jogo só será interrompido quando o jogador perder, mostrando o total de
vitórias consecutivas que ele conquistou no final do jogo.
'''
print("=-" * 13)
print('VAMOS JOGAR PAR OU ÍMPAR')
print("=-" * 13)

from random import randint

v = 0
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(1,10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    print('Você jogou {} e o computador {}. Total de {} '.format(jogador, computador, total), end='')
    print('DEU PAR' if total % 2 == 0 else 'DEU IMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU')
            break
    print('Vamos jogar novamente...')       
    print('-' * 26)
print('GAME OVER! Você venceu {} vezes.'.format(v))
    
