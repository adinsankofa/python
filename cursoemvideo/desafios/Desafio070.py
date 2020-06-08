'''
Exercício Python 070: Crie um programa que leia o nome e o preço de vários
produtos. O programa deverá perguntar se o usuário vai continuar ou não. No
final, mostre: A) qual é o total gasto na compra.
'''

print('-' * 30)
print('{:^30}'.format(' LOJA SUPER BARATÃO '))
print('-' * 30)

menorPreco = preco = totPreco = totMaiorMil = cont = 0
prodMenor = ''
while True:
    nome_produto = str(input('Nome do Produto: ')).strip()
    preco = float(input('Preço: R$ '))
    totPreco += preco
    cont += 1
    if preco > 1000:
        totMaiorMil += 1
    if cont == 1 or preco < menorPreco:
        menorPreco = preco
        prodMenor = nome_produto
    continua = str(input('Quer continuar: '))
    if continua not in 'Ss':
        break
    print('-' * 30)

print('{:-^30}'.format(' FIM DO PROGRAMA '))

print('O total da compra foi R$ {:2.2f}'.format(totPreco))
print('Temos {} produtos custando mais de R$ 1.000,00'.format(totMaiorMil))
print('O produto mais barato foi {} que custa R$ {:2.2f}'.format(prodMenor, menorPreco))
