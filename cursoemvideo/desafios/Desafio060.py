'''
Faça um programa que leia um número qualquer e mostre o seu fatorial.
'''

## FATORIAL com modulo FACTORIAL ##
from math import factorial
n = int(input('Digite um número para calcular seu Fatorial: '))
f = factorial(n)
print('O fatorial de {} é {}.'.format(n, f))



## FATORIAL com WHILE ##
n = int(input('Digite um número para calcular seu Fatorial: '))
c = n
fat = 1
print('Calculando {}! = '.format(n), end='')
while c > 0:
    print('{} '.format(c), end = '')
    print('x ' if c > 1 else '= ', end='')
    fat = fat * c
    c -= 1
print(fat)




## FATORIAL com FOR ##
n = int(input('Digite um fatorial: '))
fat = 1
print('Calculando {}'.format(n), end = '! = ')
for i in range(n, 1, -1):
    fat = fat * i
    print('{}'.format(i), end=' x ')

print('{} = '.format(1), end='')
print(fat)





