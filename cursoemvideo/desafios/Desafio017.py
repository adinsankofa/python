'''
Faça um programa que leia o comprimento do cateto oposto e do cateto adjascente de um triângulo retângulo,
calcule e mostre o comprimento da hipotenusa.
'''

from math import hypot

oposto = float(input("Qual é o comprimento do cateto oposto: "))
adjascente = float(input("Qual é o comprimento do cateto oposto: "))

hi = hypot(oposto,adjascente)

hi1 = (oposto ** 2 + adjascente ** 2) ** (1/2)

print('O valor da hipotenusa é {:.2f}'.format(hi1))