'''
Exercício Python 036: Escreva um programa para aprovar o empréstimo bancário
para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e
em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do
salário ou então o empréstimo será negado.
'''

valor_casa = float(input('Valor da casa? '))
sal_comp = float(input('Salário do comprador? '))
anos_fin = int(input('Quantos anos de financiamento? '))

minimo = sal_comp / 100 * 30

print('Para pagar uma casa de R$ {:0.2f} em {} anos a prestação será de R$ {:0.2f}'.format(valor_casa, anos_fin, valor_casa / (12 * anos_fin)))

if valor_casa / (12 * anos_fin) <= minimo:
    print('Empréstimo pode ser CONCEDIDO!')
else:
    print('Empréstimo NEGADO!')
    



