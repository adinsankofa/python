'''
O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia as um conjunto 
indeterminado de temperaturas, e informe ao final a menor e a maior temperaturas informadas, bem como a média 
das temperaturas.
'''

print('\n')

n_temp = 10
soma = 0
maior = 0
menor = 100

for i in range(1,n_temp+1):
    temperatura = int(input('Digite a %iª temperatura: '%i))
    soma += temperatura

    if temperatura > maior:
        maior = temperatura

    if temperatura < menor:
        menor = temperatura

print('\n')

print('Maior: ', maior)
print('Menor: ', menor)
print('Média: ', soma / n_temp)







