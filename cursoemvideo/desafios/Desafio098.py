"""
Exercício Python 098: Faça um programa que tenha uma função chamada contador(),
que receba três parâmetros: início, fim e passo. Seu programa tem que realizar
três contagens através da função criada:

a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada
"""


#VERSÃO GUANABARA
from time import sleep
def contador(i, f, p):
    if p < 0:
        p += -1
    if p == 0:
        p = 1
    print('-=' * 20)
    print(f'Contagem de {i} até {f} de {p} em {p}')
    sleep(2.5)

    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='')
            sleep(0.5)
            cont += p
        print('FIM!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='')
            sleep(0.5)
            cont -= p
        print('FIM!')

#Programa principal
contador(1, 10, 1)
contador(10, 0, 2)
print('-=' * 20)
print('Agora é sua vez de personalizar a contagem!')
ini = int(input('Início: '))
fim = int(input('Fim: '))
pas = int(input('Passo: '))
contador(ini, fim, pas)

        


#VERSÃO BRUNO
def conta():
    print("-=" * 20)
    from time import sleep
    print("Contagem de 1 até 10 de 1 em 1")
    for i in range(1, 11):
        sleep(0.5)
        print(f'{i}', end=" ")
    print("FIM!")
    print("-=" * 20)
    sleep(1.0)
    print("Contagem de 10 até 0 de 2 em 2")
    for i in range(10, -2, -2):
        sleep(0.5)
        print(f'{i}', end=" ")
    print("FIM!")
    print("-=" * 20)
    print("Agora é sua vez de personalizar a contagem!")
    inicio = int(input("Início: "))
    fim = int(input("Fim: "))
    passo = int(input("Passo: "))
    print("-=" * 20)
    print(f"Contagem de {inicio} até {fim} de {passo} em {passo}")
    for i in range(inicio, fim, passo):
        sleep(0.5)
        print(f'{i}', end=" ")
    print(f"{fim} FIM!")
    print("-=" * 20)

        
