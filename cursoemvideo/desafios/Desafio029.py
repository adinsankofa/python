'''
Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo
que ele foi multado. A multa vai custar R$ 7,00 por cada
Km acima do limite.
'''

velocidade = float(input('Digite a valocidade: '))

if velocidade > 80:
    print('MULTADO! Você excedeu o limite permitido que é 80Km/h')
    print('Valor da multa: R$ {:.2f}'.format((velocidade - 80) * 7,00))

print('Tenha um bom dia! Dirija com segurança!')
