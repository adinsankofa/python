'''
Faça um programa que use a função valorPagamento para determinar o valor a
ser pago por uma prestação de uma conta. O programa deverá solicitar ao
usuário o valor da prestação e o número de dias em atraso e passar estes
valores para a função valorPagamento, que calculará o valor a ser pago e
devolverá este valor ao programa que a chamou. O programa deverá então exibir
o valor a ser pago na tela. Após a execução o programa deverá voltar a pedir
outro valor de prestação e assim continuar até que seja informado um valor
igual a zero para a prestação. Neste momento o programa deverá ser encerrado,
exibindo o relatório do dia, que conterá a quantidade e o valor total de
prestações pagas no dia. O cálculo do valor a ser pago é feito da seguinte
forma. Para pagamentos sem atraso, cobrar o valor da prestação. Quando houver
atraso, cobrar 3% de multa, mais 0,1% de juros por dia de atraso.
'''

def valorPagamento(valor,atraso):

    global valor_atual
    
    for i in range(atraso+1):
        if atraso > 0:
            multa = (3 * valor / 100) * i
            juros = (0.1 * valor / 100) * i
        valor_atual = valor + multa + juros

        if atraso == 0:
            valor_atual = valor
    
    return print('Valor atualizado a pagar: R$ {:0.2f}'.format(valor_atual))



print('*************************************')
print('   C O B R A N Ç A   G E T Ú L I O   ')
print('*************************************')

valor_total = []
novo_calculo = 'S'
quantidade_prestacoes = 0
while novo_calculo == 'S' or novo_calculo == 's':
    valor_prestacao = float(input('Digite o valor da prestação: R$ '))
    dias_atraso = int(input('Dias de atraso: '))

    valorPagamento(valor_prestacao,dias_atraso)

    valor_total.append(valor_atual)
    quantidade_prestacoes += 1
    
    
    print('-' * 36)
    novo_calculo = str(input('Novo cálculo: [S - Sim] e [N - Não] '))
    print('-' * 36)


print('{:^36s}'.format('RELATÓRIO'))
print('-' * 36)
print('Prestações pagas no dia: ', quantidade_prestacoes)
print('Valor total recebido: R$ {:0.2f}'.format(sum(valor_total)))

print('-' * 36)
