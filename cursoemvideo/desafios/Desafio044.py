'''
Exercício Python 044: Elabore um programa que calcule o valor
a ser pago por um produto, considerando o seu preço normal e
condição de pagamento:
- à vista dinheiro/cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preço formal
- 3x ou mais no cartão: 20% de juros
'''

print('{:=^30}'.format(' LOJAS GUANABARA '))

preco = float(input('Preço das compras: R$ '))

print('FORMAS DE PAGAMENTO')
print('[ 1 ] à vista dinheiro / cheque')
print('[ 2 ] à vista cartão')
print('[ 3 ] 2x no cartão')
print('[ 4 ] 3x ou mais no cartão')

opcao = int(input('Qual é a opção? ' ))


if opcao == 1:
    total = preco - preco / 100 * 10
elif opcao == 2:
    total = preco - preco / 100 * 5
elif opcao == 3:
    total = preco
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R$ {:2.2f}'.format(parcela))
elif opcao == 4:
    total = preco + preco / 100 * 20
    totparc = int(input('Quantas parcelas? ' ))
    parcela = total / totparc
    print('Sua compra será parcelada em {}x de R$ {:2.2f} COM JUROS'.format(totparc,parcela))
else:
    total = 0
    print('OPÇÃO INVÁLIDA de pagamento. Tente novamente!')
print('Sua compra de R$ {:2.2f} vai custar R$ {:2.2f} no final.'.format(preco, total))
    
