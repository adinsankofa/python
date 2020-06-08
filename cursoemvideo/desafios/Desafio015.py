'''
Escreva um programa que pergunte a quantidade de Km percorridos por um carro
alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar,
sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
'''

QuantKm = float(input("Km percorridos: "))
dias = int(input("Dias de aluguel: "))
pago = (dias * 60)+(QuantKm * 0.15)
print("Valor a pagar R$ {:0.2f}".format(pago))