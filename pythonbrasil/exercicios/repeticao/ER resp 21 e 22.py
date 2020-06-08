'''
Faça um programa que peça um número inteiro e determine se ele é ou não um
número primo. Um número primo é aquele que é divisível somente por ele mesmo
e por 1.
'''

n = int(input('Digite um número: '))
div = []
for i in range(1,n+1):
    if n % i == 0:
        div.append(i)

if n + 1 == sum(div):
    a = str(div)
    print('O número',n, 'é PRIMO, pois é divisível apenas por %s e %s.'%(div[0], div[1]))
else:
    del div[-1]
    print('O número', n, 'não é PRIMO, pois é divisível por ', end='')
    for i in div:
        print('%s'%i, end = ', ')
    print('%s.'%n)
      
