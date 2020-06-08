'''
Exercício Python 050: Desenvolva um programa que leia seis números
inteiros e mostre a soma apenas daqueles que forem pares. Se o valor
digitado for ímpar, desconsidere-o.
'''

par = 0
contador = 0
for i in range(1,7):
    n = int(input('Digite {}º números inteiros: '.format(i)))
    if n % 2 == 0:
        par += n
        contador += 1

print('')
print('Você informou {} números PARES e a soma foi {}.'.format(contador, par))
print('')


