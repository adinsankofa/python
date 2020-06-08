'''
Faça um programa que leia um número inteiro e diga se ele
é ou não um número primo.
'''


n = int(input('Digite um número: '))

contador = 0
for i in range(1, n+1):
    if n % i == 0:
        contador += 1
        
print('O número {} foi divisível {} vezes'.format(n, contador))
        
if contador == 2:
    print('E por isso ele É PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO!')
