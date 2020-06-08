'''
Um posto está vendendo combustíveis com a seguinte tabela de descontos:

Álcool: até 20 litros, desconto de 3% por litro
acima de 20 litros, desconto de 5% por litro

Gasolina: até 20 litros, desconto de 4% por litro
acima de 20 litros, desconto de 6% por litro

Escreva um algoritmo que leia
o número de litros vendidos, o tipo de combustível (codificado da seguinte
forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente
sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.
'''

print('**************************************************')
print('***************** POSTO FORMIGÃO *****************')
print('**************************************************')

print('')

combustivel = input('Combustível [A = Álcool / G = Gasolina]: ')
litros = int(input('Litros: '))
preco = 0
preco_Alcool = 1.90
preco_Gasolina = 2.50
desconto = 0
desconto_valor = 0
valorapagar = 0

## ALCOOL ##
if combustivel == 'A':
    combustível = 'Alcool'
    preco = preco_Alcool
    if 0 < litros <= 20:
        desconto = preco / 100 * 3
    if litros > 20:
        desconto = preco / 100 * 5

    desconto_valor = desconto * litros

    valorapagar = preco * litros - desconto_valor

## GASOLINA ##
elif combustivel == 'G':
    combustível = 'Gasolina'
    preco = preco_Gasolina
    if 0 < litros <= 20:
        desconto = preco / 100 * 4
    if litros > 20:
        desconto = preco / 100 * 6

    desconto_valor = desconto * litros

    valorapagar = preco * litros - desconto_valor

print('\n')
print('COMBUSTÍVEL ABASTECIDO: ', combustível)
print('')
print('Valor: \t \t \t R$ {:0.2f}'.format(preco * litros))
print('Desconto (-): \t \t R$ 0{:0.2f}'.format(desconto_valor))
print('-' * 15)
print('Valor a pagar: \t \t R$ {:0.2f}'.format(valorapagar))

print('')

print('**************************************************')
print('**************************************************')
print('**************************************************')
        
               
    
