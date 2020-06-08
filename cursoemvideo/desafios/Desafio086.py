'''
Exercício Python 086: Crie um programa que declare uma matriz de dimensão 3x3
e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela,
com a formatação correta.
'''


## VERSÃO GUANABARA:
matriz = [[0,0,0],[0,0,0],[0,0,0]]
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print("=-" * 30)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()


## VERSÃO BRUNO
matriz = []
for i in range(3):
    num = []
    for c in range(3):
        num.append(int(input(f"Digite um valor para [{i}, {c}]: ")))
    matriz.append(num)
print("=-" * 30)
for i in range(len(matriz)):
	print("")
	for c in matriz[i]:
		print(f"[{c:^5}]", end=" ")


            

