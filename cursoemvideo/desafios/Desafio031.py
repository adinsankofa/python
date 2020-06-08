'''
Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem,
cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
'''

distancia = float(input('Digite a distância de sua viagem: '))

valor = 0

valor = distancia * 0.50 if distancia <= 200 else distancia *  0.45

'''
if distancia <= 200:
    valor = 0.50 * distancia
else:
    valor = 0.45 * distancia
'''

print('Valor da viagem: R$ {:.2f}'.format(valor))
