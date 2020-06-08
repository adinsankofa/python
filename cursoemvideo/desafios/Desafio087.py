'''
Exercício Python 087: Aprimore o desafio anterior, mostrando no final: 
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.
'''


## VERSÃO GUANABARA:
matriz = [[0,0,0],[0,0,0],[0,0,0]]
spar = mai = scol = 0
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print("=-" * 30)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            spar += matriz[l][c]
    print()
print("=-" * 30)
print(f"A soma dos valores pares é {spar}.")
for l in range(0, 3):
    scol += matriz[l][2]
print(f'A soma dos valores da terceira coluna é {scol}.')
for c in range(0, 3):
    if c == 0:
        mai = matriz[l][c]
    elif matriz[l][c] > mai:
        mai = matriz[l][c]
print(f"O maior valor da segunda linha é {mai}.")




## VERSÃO BRUNO
matriz = [[0,0,0],[0,0,0],[0,0,0]]
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print("=-" * 30)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print("=-" * 30)

pares = 0
soma_terceira_coluna = 0
maior_segunda_linha = 0
for l in range(0,3):
    for c in range(0,3):
        if c == 2:
            soma_terceira_coluna += matriz[l][c]
        if l == 2:
            linha2 = matriz[l][c]
            if linha2 > maior_segunda_linha:
                maior_segunda_linha = linha2
        if matriz[l][c] % 2 == 0:
            pares += matriz[l][c]
print(f"A soma dos valores pares é {pares}")
print(f"A soma dos valores da terceira coluna é {soma_terceira_coluna}")
print(f"O maior valor da segunda linha e {maior_segunda_linha}")


            

