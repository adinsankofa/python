'''
Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram
a maioridade e quantas já são maiores.
'''

print('')

from datetime import date

ano_atual = date.today().year
menor = 0
maior = 0
for i in range(1,8):
    nasc = int(input('Em que ano a {}ª pessoa nasceu? '.format(i)))
    if ano_atual - nasc >= 21:
        maior += 1
    else:
        menor += 1

print('')

print('Ao todo tivemos {} pessoas maiores de idade.'.format(maior))
print('E também tivemos {} pessoas menores de idade.'.format(menor))

print('')
