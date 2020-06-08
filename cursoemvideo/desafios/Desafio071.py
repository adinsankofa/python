'''
Exercício Python 071: Crie um programa que simule o funcionamento de um caixa
eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado
(número inteiro) e o programa vai informar quantas cédulas de cada valor
serão entregues.
'''

print('=' * 30)
print('{:^30}'.format('BANCO CEV'))
print('=' * 30)

saque = int(input('Que valor você quer sacar? R$ '))

total = saque
ced = 50
totalCed = 0
while True:
    if total >= ced:
        total -= ced
        totalCed += 1
    else:
        if totalCed > 0:
            print('Total de {} cédulas de R$ {}'.format(totalCed, ced))
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totalCed = 0
        if total == 0:
            break

