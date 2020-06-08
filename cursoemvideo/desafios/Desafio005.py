'''
Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu
antecessor.
'''

num = int(input('Digite um número: '))

print('Sucessor: {:^20}'.format(str(num + 1)))
print('Antecessor: {:^20}'.format(str(num - 1)))
