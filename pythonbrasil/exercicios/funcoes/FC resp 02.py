'''
Faça um programa para imprimir:
   1
    1   2
    1   2   3
    .....
    1   2   3   ...  n
para um n informado pelo usuário. Use uma função que receba um valor n inteiro imprima até a n-ésima linha.
'''

                    ### DIAGONAL SUPERIOR ESQUERDA ###

def matriz2(n):
    matriz = []
    for l in range(1,n+1):
        linha = []
        for c in range(l,n+1):
            linha.append(c)
        matriz.append(linha)
    for i in matriz:
        print(i)
matriz2(10)



                ### DIAGONAL INFERIOR ESQUERDA ###

def matriz2(n):
    matriz = []
    for l in range(1,n+1):
        linha = []
        for c in range(1, l+1):
            linha.append(c)
        matriz.append(linha)
    for i in matriz:
        print(i)
matriz2(10)


