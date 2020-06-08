"""
Faça um programa que pergunte o preço de três produtos e informe qual
produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.
"""

barato = 1000
num = 0

for i in range(1,4):
    preco = float(input("Digite o preço do %iº produto: " %(i)))

    if preco < barato:
        barato = preco
        num = i
    

print("")
print("Produto indicado nº %i com preço R$ %2.2f "%(num, barato))


#Abaixo fiz outro exemplo de como usar o número do contador para indicação:

"""
maior = 0
menor = 100
nmaior = 0
nmenor = 0

for i in range(1, 5):
    num = int(input("Digite o %iº número: "%(i)))

    if num > maior:
        maior = num
        nmaior = i
        
    if num < menor:
        menor = num
        nmenor = i

print("")
print("MAIOR: ", nmaior, maior)
print("MENOR: ", nmenor, menor)
"""
