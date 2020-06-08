'''
Faça um programa que mostre os n termos da Série a seguir:
 S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m.
Imprima no final a soma da série.
'''

n = int(input('Digite a quantidade de termos: '))
a = 1
b = 0
print('S = ', end="")
for i in range(1,n-2,2):
    a = a
    print('{}/{} + '.format(a,i), end='')
    b += a / i
    a += 1
c = a
d = i+2
print('{}/{} = {:0.2f}'.format(a,i+2,b+(c/d)))
