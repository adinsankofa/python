'''
Faça um Programa que peça um número inteiro e determine se ele é par ou impar.
Dica: utilize o operador módulo (resto da divisão).
'''

### ALGORITMO ###

num = int(input('Digite um número: '))

if num % 2 == 0:
    print(f'{num} e PAR')
else:
    print(f'{num} e IMPAR')




### FUNÇÃO ###

def parImpar(num):
    if num % 2 == 0:
        print(f'{num} e PAR')
    else:
        print(f'{num} e IMPAR')



