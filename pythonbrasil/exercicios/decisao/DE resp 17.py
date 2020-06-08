'''
Faça um Programa que peça um número correspondente a um determinado
ano e em seguida informe se este ano é ou não bissexto.
'''

n = int(input('Digite um ano: '))

if n % 400 == 0 or n % 4 == 0 and n % 100 != 0:
    print(n, 'é Bissexto')
else:
    print(n, 'não e Bissexto')
    


    
