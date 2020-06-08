'''
Faça um programa, com uma função que necessite de um argumento. A função
retorna o valor de caractere ‘P’, se seu argumento for positivo, e ‘N’, se
seu argumento for zero ou negativo.
'''

def PosNeg(a,b):
    x = a + b
    if x >= 0:
        print('P')
    else:
        if x < 0:
            print('N')
            
        
