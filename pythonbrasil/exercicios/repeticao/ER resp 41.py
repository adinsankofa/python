'''
Faça um programa que receba o valor de uma dívida e mostre uma tabela com os seguintes dados:
valor da dívida, valor dos juros, quantidade de parcelas e valor da parcela.
Os juros e a quantidade de parcelas seguem a tabela abaixo:
Quantidade de Parcelas  % de Juros sobre o valor inicial da dívida
1       0
3       10
6       15
9       20
12      25
Exemplo de saída do programa:
Valor da Dívida Valor dos Juros Quantidade de Parcelas  Valor da Parcela
R$ 1.000,00     0               1                       R$  1.000,00
R$ 1.100,00     100             3                       R$    366,00
R$ 1.150,00     150             6                       R$    191,67
'''

valor_da_parcela = 0
juro = 0

divida = float(input('Digite o valor da divida: R$ '))
juros = float(input('Juros (%): '))
parcelas = int(input('Parcelas: '))
print('')
print('VALOR DA DÍVIDA \t VALOR DOS JUROS \t QUANTIDADE DE PARCELAS \t VALOR DA PARCELA')
for i in range(1, parcelas+1):
    divida += valor_da_parcela
    juro += divida / 100 * juros
    valor_da_parcela += parcelas + juro
    print('  R$ {:>7.2f}\t\t   R$ {:>7.2f}\t\t\t   {:>2}\t\t\t   R$ {:>8.2f}'.format(divida, juro, i, valor_da_parcela))
print('')

              



