'''
Escreva um programa que converta uma temperatura digitada em ºC e converta para ºF
'''

temperatura_em_C = float(input("Digite a temperatura em Cº: "))

temperatura_em_F = (temperatura_em_C * 1.8)+32

print('A temperatura de {:2.0f} ºC convertido para Fahrenheit é {:2.0f} ºF.'.format(temperatura_em_C,temperatura_em_F))