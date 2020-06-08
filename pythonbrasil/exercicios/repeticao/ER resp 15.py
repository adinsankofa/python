'''
A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,...
Faça um programa capaz de gerar a série até o n−ésimo termo.
'''

rep = 1
soma = 0
ultimo = 0
penultimo = 0 

while rep <= 50:

    if rep == 1:
        print("0")
    else:
        if rep == 2:
            print("1")
        else:
            if rep == 3:
                print("1")
                ultimo = 1
                penultimo = 1
            else:
                soma = ultimo + penultimo
                print(soma)
                penultimo = ultimo
                ultimo = soma
 
    rep = rep + 1
