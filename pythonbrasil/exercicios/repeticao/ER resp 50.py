'''
Sendo H= 1 + 1/2 + 1/3 + 1/4 + ... + 1/N, Faça um programa que calcule o
valor de H com N termos.
'''


                ### FATORIAL ###

n = int(input('Digite a quantidade de termos: '))
i = 1
fat = 1
print('H = {}/{}'.format(n,i), end=' + ')
while i < n+1:
    fat *= i
    i += 1
for j in range(2,n):
    print('{}/{}'.format(n, j), end=' + ')
print('{}/{} = '.format(n,n,n,i), end='')
print(fat)

