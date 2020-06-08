'''
Faça um programa que leia 5 números e informe a soma e a média dos números.
'''

# Utilizando variável soma

numeros = 5
soma = 0

for i in range(1,numeros + 1):
    num = int(input("Digite o %iº número: "%(i)))
    soma += num

print("")
print("SOMA: ", soma)
print("MÉDIA: ", soma / numeros)
print("")



# Somando já na variável num

numeros = 5
num = 0

for i in range(1,numeros + 1):
    num += int(input("Digite o %iº número: "%(i)))

print("")
print("SOMA: ", num)
print("MÉDIA: ", num / numeros)
print("")
