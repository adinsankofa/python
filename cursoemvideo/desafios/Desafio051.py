'''
Exercício Python 051: Desenvolva um programa que leia o primeiro termo e
a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.
'''

print('=' * 30)
print('{:^30}'.format('10 TERMOS DE UMA PA'))
print('=' * 30)

pt = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = pt + (10 - 1) * razao
for i in range(pt, decimo + razao, razao):
    print(i, end=' -> ')

print('ACABOU')
