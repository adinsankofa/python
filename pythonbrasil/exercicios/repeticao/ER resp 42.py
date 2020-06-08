'''
Faça um programa que leia uma quantidade indeterminada de números positivos e
conte quantos deles estão nos seguintes intervalos: [0-25], [26-50], [51-75]
e [76-100]. A entrada de dados deverá terminar quando for lido um número negativo.
'''

menor = int(input('Menor: '))
while menor >= 0:
    intervalo = 0
    if menor >= 0:
        maior = int(input('Maior: '))

    if maior >= 0:
        for i in range(maior + 1):
            intervalo = maior - menor
        print('Valor no intervalo: {}'.format(intervalo))
        print('')

    menor = int(input('Menor: '))



