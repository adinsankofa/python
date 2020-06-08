'''
Exercício Python 065: Crie um programa que leia vários números
inteiros pelo teclado. No final da execução, mostre a média entre
todos os valores e qual foi o maior e o menor valores lidos. O programa
deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
'''

num = int(input('Digite um número: '))
resposta = str(input('Quer continuar? ')).upper().strip()[0]
cont = 1
soma = maior = num
menor = maior
while resposta in 'Ss':
    num = int(input('Digite um número: '))
    resposta = str(input('Quer continuar? ')).upper().strip()[0]
    cont += 1
    soma += num
    if num > maior:
        maior = num
    if num < menor:
        menor = num

media = soma / cont

print('Você digitou {} números e a média foi {}'.format(cont, media))
print('O maior valor foi {} e o menor foi {}.'.format(maior, menor))




    
    
