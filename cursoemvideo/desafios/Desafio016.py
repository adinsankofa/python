'Crie um número que leia uma número Real qualquer pelo teclado e mostre na tela sua porção inteira'

'''
from math import trunc
num = float(input('Digite um número: '))
print('O número {} tem a parte inteira {}'.format(num,trunc(num)))
'''

num = float(input('Digite um valor: '))
print('O valor digitado foi {} e sua porção inteira é {}.'.format(num,int(num)))



