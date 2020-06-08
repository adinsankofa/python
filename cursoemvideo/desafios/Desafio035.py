'''
Desenvolva um programa que leia o comprimento de três retas
e diga ao usuário se elas podem ou não formar um triângulo.
'''

print('-=' * 20)
print('ANALISADOR DE TRIÂNGULOS')
print('-=' * 20)

r1 = float(input('Primeiro segimento: '))
r2 = float(input('Segundo segimento: '))
r3 = float(input('Terceiro segimento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos PODEM FORMAR triângulo!')
else:
    print('Os segmentos acima NÃO PODE FORMAR triângulo!')
