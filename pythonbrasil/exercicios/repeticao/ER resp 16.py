'''
A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,...
Faça um programa que gere a série até que o valor seja maior que 500.
'''

elementos = 20

a = 0
b = 1
c = 0
for i in range(elementos + 1):
    fib = a + b
    if fib < 500:
        print(fib)
    a = b
    b = fib

        
