'''
Exercício Python 079: Crie um programa onde o usuário possa digitar vários
valores numéricos e cadastre-os em uma lista. Caso o número já exista lá
dentro, ele não será adicionado. No final, serão exibidos todos os valores
únicos digitados, em ordem crescente.
'''

# VERSÃO GUANABARA:
números = list()
while True:
    n = (int(input("Digite um valor: ")))
    if n not in números:
        números.append(n)
        print("Valor adicionado com sucesso...")
    else:
        print("Valor repetido, não vou adicionar!")
    r = str(input("Quer continuar? [S/N] "))
    if r in 'Nn':
        break
print("-=" * 30)
números.sort()
print(f"Você digitou os valores: {números}")



# VERSÃO BRUNO:
valores = []
while True:
    valor = (int(input("Digite um valor: ")))
    if valor not in valores:
        valores.append(valor)
        print("Valor adicionado com sucesso...")
    else:
        print("Valor repetido, não vou adicionar!")
    op = str(input("Quer continuar? [S/N] "))
    if op in 'Nn':
        break
    else:
        pass
print("-=" * 30)
valores.sort()
print(f"Você digitou os valores: {valores}")

