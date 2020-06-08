'''
Encontrar números primos é uma tarefa difícil. Faça um programa que gera
uma lista dos números primos existentes entre 1 e um número inteiro
informado pelo usuário.
'''
      

                        ### ALGORITMO ###

n = 10
lista_geral = []
primos = []

for i in range(1,n+1):
    for j in range(1,n+1):
        if i % j == 0:
            lista_geral.append(i)

for i in lista_geral:
    if lista_geral.count(i) == 2:
        primos.append(i)

print('PRIMOS: ', end = '')
for i in range(1,len(primos),2):
	print(primos[i], end = ', ')





                         ### FUNÇÃO ###

def primo(n):
    lista_geral = []
    primos = []

    for i in range(1,n+1):
        for j in range(1,n+1):
            if i % j == 0:
                lista_geral.append(i)

    for i in lista_geral:
        if lista_geral.count(i) == 2:
            primos.append(i)

    print('PRIMOS: ', end = '')
    for i in range(1,len(primos),2):
        print(primos[i], end = ', ')



