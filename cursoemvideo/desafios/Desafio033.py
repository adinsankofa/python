'''
Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
'''

a = int(input('Digite um valor: '))
b = int(input('Digite um valor: '))
c = int(input('Digite um valor: '))

menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c


maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c


print('MAIOR: {}'.format(maior))
print('MENOR: {}'.format(menor))
    

