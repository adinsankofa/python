'''
Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário.
O programa deverá mostrar também o número de divisões que ele executou para encontrar os números primos.
Serão avaliados o funcionamento, o estilo e o número de testes (divisões) executados.
'''


n = int(input('Digite o número limite: '))
div = 0
primos = []
a = []
for i in range(1,n+1):
    a = []   
    for j in range(1,n+1):
        if i % j == 0:
            div += 1
            a.append(i)

        if sum(a) == i + j:
            if a.count(i) == 2:
                primos.append(i)
       
print('')
print('Os números primos até %i são'%n, end = ' ')
for x in primos:
    print(x, end = ', ')
print('encontrados através de %i divisões. '%div, end = ' ')
print('\n')
