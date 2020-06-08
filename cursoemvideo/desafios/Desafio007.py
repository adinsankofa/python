'''
Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média
'''

nota1 = float(input('Digite a 1ª nota: '))
nota2 = float(input('Digite a 2ª nota: '))

media = (nota1 + nota2)/2

print("Média: {:0.2f}".format(media))
