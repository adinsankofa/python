'''
Faça um programa que leia uma angulo qualquer e mostre em sua tela o valor do seno, cosseno e tangente angulo
'''

from math import radians, sin, cos, tan
ângulo = float(input('Digite o angulo que você deseja: '))

seno = math.sin(math.radians(ângulo))
print('O ângulo de {} tem o SENO de {:.2f}'.format(ângulo,seno))

cosseno = math.cos(math.radians(ângulo))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(ângulo,cosseno))

tangente = math.tan(math.radians(ângulo))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(ângulo,tangente))