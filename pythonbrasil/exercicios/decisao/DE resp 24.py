'''
Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja
realizar. O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
par ou ímpar;
positivo ou negativo;
inteiro ou decimal.
'''

n = 2
num = 0

for i in range(1,n+1):
    num += float(input('Digite o {}º número: '.format(i)))

print('')

if num % 2 == 0:
    print(f'{num} é PAR')
else:
    print(f'{num} é IMPAR')


print('')


if num > 0:
    print(f'{num} é POSITIVO')
else:
    print(f'{num} é NEGATIVO')


print('')


a = num // 1

if num - a == 0:
    b = int(num)
    print('{0} é INTEIRO'.format(b))
else:
    print('{0} é DECIMAL'.format(num))






    
               
