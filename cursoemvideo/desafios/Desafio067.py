'''
Exercício Python 067: Faça um programa que mostre a tabuada de vários números,
um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido
quando o número solicitado for negativo.
'''

### SEM True e Break

num = int(input('Quer ver a tabuada de qual valor? '))
while num >= 0:
    print('-' * 35)
    for cont in range(1,11):
        print('{} x {} = {}'.format(num, cont, num * cont))
    print('-' * 35)
    num = int(input('Quer ver a tabuada de qual valor? '))

print('-' * 35)
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')

                   
### COM True e Break
while True:
    print('-' * 35)
    for cont in range(1,11):
        print('{} x {} = {}'.format(num, cont, num * cont))
    print('-' * 35)
    num = int(input('Quer ver a tabuada de qual valor? '))
    if num < 0:
        break
print('-' * 35)
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
        
