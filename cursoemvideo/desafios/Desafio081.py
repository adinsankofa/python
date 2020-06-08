'''
Exercício Python 081: Crie um programa que vai ler vários números e colocar em
uma lista. Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.
'''


## VERSÃO GUANABARA:
valores=[]
while True: 
    valores.append(int(input("Digite um valor: ")))
    continua = str(input("Quer continuar? [S/N] "))
    if continua in "nN":
        break
print("=-" * 30)
print(f"Você digitou {len(valores)} elementos.")
valores.sort(reverse=True)
print(f"Os valores em ordem descrescente são: {valores}")
if 5 in valores:
    print("O valor 5 faz parte da lista!")
else:
    print("O valor 5 não foi encontrado na lista!")



## VERSÃO BRUNO:
valores=[]
while True: 
    valores.append(int(input("Digite um valor: ")))
    continua = str(input("Quer continuar? [S/N] "))
    if continua in "nN":
        break
print("=-" * 30)
print(f"Você digitou {len(valores)} elementos.")
valores.sort(reverse=True)
print(f"Os valores em ordem descrescente são: {valores}")
if 5 in valores:
    print("O valor 5 faz parte da lista!")
else:
    print("O valor 5 não faz parte da lista!")


    
   

            

