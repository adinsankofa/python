'''
O Sr. Manoel Joaquim expandiu seus negócios para além dos negócios de 1,99 e agora possui uma loja
de conveniências. Faça um programa que implemente uma caixa registradora rudimentar. O programa deverá
receber um número desconhecido de valores referentes aos preços das mercadorias. Um valor zero deve ser
informado pelo operador para indicar o final da compra. O programa deve então mostrar o total da compra
e perguntar o valor em dinheiro que o cliente forneceu, para então calcular e mostrar o valor do troco.
Após esta operação, o programa deverá voltar ao ponto inicial, para registrar a próxima compra. A saída
deve ser conforme o exemplo abaixo:

Lojas Tabajara 
Produto 1: R$ 2.20
Produto 2: R$ 5.80
Produto 3: R$ 0
Total: R$ 9.00
Dinheiro: R$ 20.00
Troco: R$ 11.00
'''


fechar_caixa = 'S'

while fechar_caixa == 'S' or fechar_caixa == 's':

    cont = 1
    total = 0
    produto = 1

    print('\n')
    print('====================================================')
    print('================== LOJAS TABAJARA ==================')
    print('====================================================')
    print('')

    while produto > 0:

        produto = float(input('\t\t Produto %i: R$ '%(cont)))
        cont += 1
        total += produto

    print('\t\t', '-' * 15)
    print('\t\t Total: R$ %0.2f'%total)
    print('')
    dinheiro = int(input('\t\t Dinheiro: R$ '))
    print('')
    print('\t\t Troco: R$ %0.2f '%(dinheiro - total))

    print('\n')

    fechar_caixa = str(input('\t Fechar conta / proximo cliente: '))

    print('')
    

print('')
print('====================================================')
print('====================================================')
print('====================================================')
