'''
Faça um Programa que peça as quatro notas de 10 alunos, calcule e
armazene num vetor a média de cada aluno, imprima o número de alunos
com média maior ou igual a 7.0.
'''

alunos = 2
nota = 0
soma = 0

for i in range(1,3):
    notas = []
    for j in range(1,3):
        nota += float(input("Digite a %iª nota do aluno %i: " %(i, j)))
        nota /= 2
        notas.append(nota)

for media in notas:
    if media > 7:
        soma += 1
        
print("O número de alunos com média maior que 7.00 foi de %i." %soma)
    


    
