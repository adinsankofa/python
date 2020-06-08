'''
O cardápio de uma lanchonete é o seguinte:
Especificação   Código  Preço
Cachorro Quente 100     R$ 1,20
Bauru Simples   101     R$ 1,30
Bauru com ovo   102     R$ 1,50
Hambúrguer      103     R$ 1,20
Cheeseburguer   104     R$ 1,30
Refrigerante    105     R$ 1,00
Faça um programa que leia o código dos itens pedidos e as quantidades
desejadas. Calcule e mostre o valor a ser pago por item (preço * quantidade)
e o total geral do pedido. Considere que o cliente deve informar quando o
pedido deve ser encerrado.
'''

especificacao=['Cachorro Quente', 'Bauru Simples   ', 'Bauru com ovo   ', 'Hambúrger       ', 'Cheeseburguer  ', 'Refrigerante      ']
preco=[1.20, 1.30, 1.50, 1.20, 1.30, 1.00]
cliente_encerra = 's'
cod = 1
codigo = []
pedido = []
valor = []

while cod != 0:
    if cliente_encerra != 'n':
        cod = int(input('Digite o codigo do produto: '))

        if cod == 100:
            codigo.append(100)
            pedido.append(especificacao[0])
            valor.append(preco[0])
            
        if cod == 101:
            codigo.append(101)
            pedido.append(especificacao[1])
            valor.append(preco[1])
            
        if cod == 102:
            codigo.append(102)
            pedido.append(especificacao[2])
            valor.append(preco[2])
            
        if cod == 103:
            codigo.append(103)
            pedido.append(especificacao[3])
            valor.append(preco[3])
            
        if cod == 104:
            codigo.append(104)
            pedido.append(especificacao[4])
            valor.append(preco[4])
            
        if cod == 105:
            codigo.append(105)
            pedido.append(especificacao[5])
            valor.append(preco[5])

print('\n')
        
print('ESPECIFICAÇÃO \t\t', 'CÓDIGO \t', ' PREÇO')
for i in range(len(pedido)):
    print(pedido[i], '\t   {:} \t\t R$ {:^0.2f}'.format(codigo[i],  valor[i]))

print('\t\t', '-' * 20)

print('\t\t Valor à pagar: R$ {:0.2f}'.format(sum(valor)))

    





