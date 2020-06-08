'''
Exercício Python 048: Faça um programa que calcule a soma entre todos os
números que são múltiplos de três e que se encontram no intervalo de 1 até 500.
'''

contador = 0
soma = 0
for i in range(1,501,2):
    if i % 3 == 0:
        soma += i
        contador += 1 

print('A soma de todos os {} valores solicitados é {}.'.format(contador, soma))

