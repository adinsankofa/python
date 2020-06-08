'''
Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário,
com 15% de aumento.
'''

salario = float(input('Digite o salário atual: R$ '))

aumento = salario * 0.15

print('Novo salário: R$ {:0.2f}'.format(salario + aumento))