'''
Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.
'''


## VERSÃO GUANABARA:
num = (int(input("Digite um número: ")),
       int(input("Digite outro número: ")),
       int(input("Digite mais um número: ")),
       int(input("Digite o último número: ")))

print(f"O valor 9 apareceu {num.count(9)} vezes")
if 3 in num:
    print(f"O valor 3 apareceu na {num.index(3)+1}ª posição")
else:
    print("O valor 3 não foi digitado em nenhuma posição")
print(f"Os valores pares digitados foram ", end="")
for n in num:
    if n % 2 == 0:
        print(n, end="  ")
    else:
        pass



## VERSÃO BRUNO:
varia = ['um', 'outro', 'mais um', 'último']
tupla=()
for i in range(4):
    num = int(input(f"Digite {varia[i]} número: "))
    tupla = tupla + (num,)
print("Você digitou os valores:", (tupla))

vezes = 0
for i in range(len(tupla)):
    #x = tupla.count(tupla[i])
    x = tupla[i]
    if x == 9:
        vezes += 1
    else:
        pass

for i in range(len(tupla)):
    if tupla[i] == 3:
        primeiro = i
        break
    else:
        pass

par = 0
for i in tupla:
    if i % 2 == 0:
        par += 1
    else:
        pass

print(f"O valor 9 apareceu {vezes} vezes")
print(f"O valor 3 apareceu na {primeiro}ª posição")
print(f"Os valores pares digitados foram {par}")

