'''
Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com
5% de desconto
'''

preco_antigo = float(input('Digite o preço sem desconto: R$ '))

desconto = preco_antigo / 100 * 5

print('O novo valor com desconto de 5% equivalentes a R$ {:0.2f} será de R$ {:0.2f}'.format(desconto,preco_antigo-desconto))