'''
Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre,
e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
Média de Aproveitamento  Conceito
  Entre 9.0 e 10.0        A
  Entre 7.5 e 9.0         B
  Entre 6.0 e 7.5         C
  Entre 4.0 e 6.0         D
  Entre 4.0 e zero        E
O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o
conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.
'''

elementos = 2
nota = 0
soma = 0
notas = []
conceito = ""
resultado = ""

for i in range(1,elementos + 1):
    nota = float(input("Digite a %iº nota: "%(i)))
    notas.append(nota)
    soma += nota

media = soma / elementos


if media >= 9:
    conceito = "A"
    resultado = "APROVADO"
    
elif 7.5 <= media < 9:
    conceito = "B"
    resultado = "APROVADO"
    
elif 6 <= media < 7.5:    
    conceito = "C"
    resultado = "APROVADO"
    
elif 4 <= media < 6:
    conceito = "D"
    resultado = "REPROVADO"
    
elif 4 < media:
    conceito = "E"
    resultado = "REPROVADO"

print("")   
print("--------------------- B O L E T I M ---------------------")
print("Notas: ", (notas))
print("Média: %0.2f"%media)
print("Conceito: ", conceito)
print("Resultado: ", resultado)
print("---------------------------------------------------------")
    

                 

