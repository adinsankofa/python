'''
Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.
'''


## VERSÃO GUANABARA:
temp = []
princ = []
mai = men = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(princ) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    princ.append(temp[:])
    temp.clear()
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print('-=' * 30)
print(f'Ao todo, você cadastrou {len(princ)} pessoas. ')
print(f'O maior peso foi de {mai}Kg. Peso de ', end='')
for p in princ:
    if p[1] == mai:
        print(f'[{p[0]}]', end='')
print()
print(f'O menor peso foi de {men}Kg. Peso de ', end='')




## VERSÃO BRUNO:
nome = list()
peso = list()
maior = list()
menor = list()
while True:
    nome.append(str(input("Nome: ")))
    peso.append(float(input("Peso: ")))
    cont = str(input("Quer continuar: [S/N]")).upper()
    if "N" in cont:
        break
    else:
        pass
for i in range(len(peso)):
    if peso[i] == max(peso):
        maior.append(nome[i])
    if peso[i] == min(peso):
        menor.append(nome[i])
print('-=' * 30)        
print(f"Ao todo, você cadastro {len(nome)} pessoas.")
print(f"O maior peso foi {max(peso)}Kg. Peso de {maior}")
print(f"O menor peso foi {min(peso)}Kg. Peso de {menor}")



    
   

            

