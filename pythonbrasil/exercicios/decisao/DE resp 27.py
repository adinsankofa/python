'''
Uma fruteira está vendendo frutas com a seguinte tabela de preços:
                     Até 5 Kg           Acima de 5 Kg
Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
Se o cliente comprar mais de 8 Kg em frutas ou o valor total da
compra ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre
este total. Escreva um algoritmo para ler a quantidade (em Kg) de morangos
e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo
cliente.
'''

print('**************************************************************')
print('********************* QUITANDA DO CARLÃO *********************')
print('**************************************************************')


morango = 0
maca = 0
kg_morango = 2.50
kg_maca = 1.80
descMor = 0
descMac = 0

print('')
morango += int(input('\t\t Quantidade de MORANGOS: '))
maca += int(input('\t\t   Quantidade de MAÇÃS: '))
print('')

if morango > 5:
    kg_morango = 2.20

if maca > 5:
    kg_maca = 1.50


valorMor = kg_morango * morango
valorMac = kg_maca * maca

if morango > 8 or valorMor > 25:
    descMor = valorMor / 100 * 10

if maca > 8 or valorMac > 25:    
    descMac = valorMac / 100 * 10
    

print('CUPOM FISCAL: ')
print('-' * 12)
print('Morangos: \t\t {:2f} Kg \t\t R$ {:0.2f}'.format(morango,valorMor))
if descMor > 0:
    print('Desconto Morango (-): \t\t\t\t R$ -{:0.2f}'.format(descMor))
print('Maçãs: \t\t\t {:2f} Kg \t\t R$ {:0.2f}'.format(maca,valorMac))
if descMor > 0:
    print('Desconto Maçã (-):   \t\t\t\t R$ -{:0.2f}'.format(descMac))
print('-' * 20)
print('Total a pagar: \t\t\t R$  {:0.2f}'.format((valorMor - descMor) + (valorMac - descMac)))

print('\n')

print('**************************************************************')
print('**************************************************************')
print('**************************************************************')
