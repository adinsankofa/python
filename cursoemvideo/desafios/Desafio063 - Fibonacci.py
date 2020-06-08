'''
Exercício Python 063: Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N
primeiros elementos de uma Sequência de Fibonacci.
'''

print('-' * 25)
print('Sequência de Fibonacci')
print('-' * 25)

n = int(input('Quantas sequências você quer? '))

t1 = 0
t2 = 1
cont = 3
print('0  1', end = '  ')
while cont < n+1:
    t3 = t1 + t2
    print(t3, end='  ')
    t1 = t2
    t2 = t3
    cont += 1



    
    


