'''
Faça um Programa que peça a idade e a altura de 5 pessoas,
armazene cada informação no seu respectivo vetor. Imprima
a idade e a altura na ordem inversa a ordem lida.
'''

pessoas = 5

idade = []
altura = []

for i in range(1, pessoas + 1):
    ida = int(input("Digite a %iª idade da pessoa nº %i: "%(i,i)))
    alt = float(input("Digite a %iª altura da pessoa nº %i: "%(i,i)))

    idade.append(ida)
    altura.append(alt)

'''

#Utilizando o SLICE
idade_invertida = idade[::-1]
altura_invertida = altura[::-1]

for i in range(pessoas):
    print("Idade %i: %i"%(pessoas - i, idade_invertida[i]))
    print("Alturas %i: %.2f"%(pessoas - i, altura_invertida[i]))

#Utiliando o método RANGE
for i in range(pessoas-1,-1,-1):
    print("Idade %i: %i"%(i + 1, idade[i]))
    print("Alturas %i: %.2f"%(i + 1, altura[i]))

'''

#Utilizando o método REVERSE

idade.reverse()
altura.reverse()

for i in range(pessoas):
    print("Idade %i: %i"%(pessoas - i, idade[i]))
    print("Alturas %i: %.2f"%(pessoas - i, altura[i]))
