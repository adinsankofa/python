'''
Faça um programa que peça dois números, base e expoente, calcule e mostre
o primeiro número elevado ao segundo número. Não utilize a função de potência
da linguagem.
'''

base = int(input("Digite a base: "))
expoente = int(input("Digite o expoente: "))

print("")

for i in range(1, expoente + 1):
    print("base(%i) x expoente(%i) = %i" %(base, i, base ** i))

print("")

print("Valor total: %i"%(base ** expoente))



    
    
