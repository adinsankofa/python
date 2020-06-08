'''
Faça um programa que peça um numero inteiro positivo e em seguida mostre este numero invertido.
Exemplo:
 12376489
  => 98467321

'''

                            ### ALGORITMO ###

num = int(input('Digite o número: '))

for i in range(num, 0,-1):
    print(i, end = ' ')



                            ### FUNÇÃO ###

def reverse(num):
    for i in range(num, 0,-1):
        print(i, end = ' ')
