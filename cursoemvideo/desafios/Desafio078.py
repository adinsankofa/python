'''
Exercício Python 078: Faça um programa que leia 5 valores numéricos
e guarde-os em uma lista. No final, mostre qual foi o maior e o menor
valor digitado e as suas respectivas posições na lista.
'''

# VERSÃO GUANABARA:
listanum = []
mai = 0
men = 0
for c in range(0,5):
    listanum.append(int(input(f"Digite um valor para a Posição {c}: ")))
    if c == 0:
        mai = men = listanum[c]
    else:
        if listanum[c] > mai:
            mai = listanum[c]
        if listanum[c] < men:
            men = listanum[c]

print('=-' * 30)
print(f"Você digitou os valores: {listanum}")
print(f"O maior valor digitado foi {mai} nas posições: ", end="")
for i, v in enumerate(listanum):
    if v == mai:
        print(f"{i}...", end="")
print()
print(f"O menor valor digitado foi {men} nas posições: ", end="")
for i, v in enumerate(listanum):
    if v == men:
        print(f"{i}...", end="")
print()




# VERSÃO BRUNO:
valores = []
for i in range(5):
    valores.append(int(input(f"Digite um valor para a Posição {i}: ")))

maior = max(valores)
menor = min(valores)
maiores = []
menores = []
for i in range(len(valores)):    
    if valores[i] == menor:
        menores.append(i)
    else:
        pass

    if valores[i] == maior:
        maiores.append(i)
    else:
        pass


print(f"Você digitou os valores: {valores}")
print(f"O maior valor digitado foi {maior} nas posições: ", end="")
for i in maiores:
    print(f"{i}...", end="")


print(f"\nO menor valor digitado foi {menor} nas posições: ", end="")
for i in menores:
    print(f"{i}...", end="")


