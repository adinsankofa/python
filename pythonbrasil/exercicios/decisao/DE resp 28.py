'''
O Hipermercado Tabajara está com uma promoção de carnes que é imperdível.
Confira:
                     Até 5 Kg           Acima de 5 Kg
File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
Para atender a todos os clientes, cada cliente poderá levar apenas um dos
tipos de carne da promoção, porém não há limites para a quantidade de carne
por cliente. Se compra for feita no cartão Tabajara o cliente receberá ainda
um desconto de 5% sobre o total a compra. Escreva um programa que peça o tipo
e a quantidade de carne comprada pelo usuário e gere um cupom fiscal, contendo
as informações da compra: tipo e quantidade de carne, preço total, tipo de
pagamento, valor do desconto e valor a pagar.
'''

mais_cliente = 'n'
cartao_tabajara = ''
quantidade = 0
carne1 = 4.90
carne2 = 5.90
carne3 = 6.90
cliente = []
preco = 0
num = 0
carne = ''
desconto = 0

print('=' * 60)

while mais_cliente == 'n' or mais_cliente == 'N':
       
    num += 1
    print('Cliente nº ',num)
    quantidade = float(input('Quantidade: '))

    tipo = int(input('Tipo de carne [1 - Filé Duplo] [2 - Alcatra] [3 - Picanha]: '))

    if quantidade > 5:
        carne1 = 5.80
        carne2 = 6.80
        carne3 = 7.80

    if tipo == 1:
        carne = 'Filé Duplo'
        preco = carne1 * quantidade
    elif tipo == 2:
        carne = 'Alcatra'
        preco = carne2 * quantidade
    elif tipo == 3:
        carne = 'Picanha'
        preco = carne3 * quantidade
  
    mais_cliente = str(input('Fechar conta: '))

    print('=' * 60)


print('\t\t  CUMPOM FISCAL')
print('\t\t','-' * 15)
print('')

print('PRODUTO \t QUANTIDADE \t PREÇO')
print(carne,'\t   {:0.2f}kg'.format(quantidade),'\t R$ {:0.2f}'.format(preco))
print('')
pagamento = int(input('Forma de pagamento [1 - Dinheiro] [2 - Cartão Tabajara]: '))
if pagamento == 2:
    desconto = preco / 100 * 5
print('')
if pagamento == 2:
    print('\t      Desconto (-) R$ {:0.2f}'.format(desconto))
print('\t     ','-' * 20)
print('\t     Valor a pagar: R$ {:0.2f}'.format(preco - desconto))



    
        

    

        
