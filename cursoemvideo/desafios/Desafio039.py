'''
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo
com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora
exata de se alistar ou se já passou do tempo do alistamento. Seu programa
também deverá mostrar o tempo que falta ou que passou do prazo.
'''

from datetime import date

atual = date.today().year

nasc = int(input('Ano de nascimento: '))

idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}.'.format(nasc,idade,atual))

if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    print('Você não tem 18 anos. Ainda faltam {} anos para o alistamento militar.'.format(18 - idade))
    print('Seu alistamento será em {}.'.format(atual + (18+idade)))
elif idade > 18:
    print('Você deveria ter se alistado há {} anos.'.format(idade - 18))
    print('Seu alistamento foi em {}.'.format(atual - (idade-18)))

