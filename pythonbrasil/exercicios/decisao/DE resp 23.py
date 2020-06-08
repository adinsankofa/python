'''
Faça um Programa que peça um número e informe se o número é inteiro ou decimal.
Dica: utilize uma função de arredondamento.
'''

                                ### ALGORITMO ###

num = float(input('Digite um número: '))

a = num // 1

if num - a == 0:
    b = int(num)
    print('{0} é INTEIRO'.format(b))
else:
    print('{0} é DECIMAL'.format(num))






                                  ### FUNÇÃO ###

def intDec(num):

    a = num // 1

    if num - a == 0:
        b = int(num)
        print('{0} é INTEIRO'.format(b))
    else:
        print('{0} é DECIMAL'.format(num))





