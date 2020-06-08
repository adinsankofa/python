'''
Faça um programa para imprimir:
   1
    2   2
    3   3   3
    .....
    n   n   n   n   n   n  ... n
para um n informado pelo usuário. Use uma
função que receba um valor n inteiro e imprima até a n-ésima linha.
'''

def matrizN(n):

    l=1
    c=n
    matriz=[]
    for l in range(l):
        for c in range(1,c+1):
            matriz.append([l+c]*c)

    for i in matriz:
        print(i)
    





    
        
