'''
Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.
'''


elementos = 5


menor = 1000
maior = 0
soma = 0
for i in range(1, elementos+1):
    n = int(input("Digite um número: "))

    if n >= 1000 or n <= 0:
        print("Núméro inválido")
        print("")
        
    if n > maior:
        if n <= 1000:
            maior = n

    if n < menor:
        if n > 0: 
            menor = n

    if 1000 > n > 0:
        soma += n


print("")
print("MAIOR: ", maior)
print("MENOR: ", menor)
print("Soma (MAIOR + MENOR): ", maior + menor)
print("Soma dos valores: ", soma)
print("")
