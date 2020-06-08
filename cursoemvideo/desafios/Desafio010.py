'''
Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre
quantos dolares ela pode comprar
'''

dindin_carteira = float(input('Digite quanto você tem na carteira: R$ '))

dolar = 3.27 * dindin_carteira

print('O valor de R$ {:0.2f} convertido em dolar dará R$ {:0.2f}'.format(dindin_carteira, dolar))
