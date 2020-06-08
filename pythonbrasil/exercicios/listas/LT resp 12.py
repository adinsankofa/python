'''
Foram anotadas as idades e alturas de 30 alunos.
Faça um Programa que determine quantos alunos com mais de 13
anos possuem altura inferior à média de altura desses alunos.
'''

elementos = 3

idade = []
altura = []
aluno = []

alt = 0
ida = 0
media = 0
mediaTot = 0
soma = 0


for i in range(1, elementos + 1):
    print("")
    alu = str(input("Aluno %i: "%(i)))
    aluno.append(alu)
    
    for j in range(1):

        ida = int(input("Idade: " ))
        idade.append(ida)

       
        alt = float(input("Altura: " ))
        soma += alt
        altura.append(alt)


    media = soma / elementos

  
for i in range(elementos):
    if altura[i] < media and idade[i] > 13:
        mediaTot += 1

 
print("")
print("ALUNO", "   \t\t", "IDADE", "\t\t", "ALTURA")

for i in range(elementos):
    print(aluno[i],"   \t\t", idade[i],"\t\t", altura[i],"m")

print("")
print("Média de Altura: %2.2f "%media)
print("")

A = ("Nenhum (%i) aluno é maior que 13 anos e tem altura menor que a média de %2.2fm"%(mediaTot, media))
B = ("Apenas %i aluno é maior que 13 anos e tem altura menor que a média de %2.2fm"%(mediaTot, media))
C = ("Serão %i alunos maiores que 13 anos e com altura menor que a média de %2.2fm"%(mediaTot, media))

if mediaTot == 0:
    print(A)
elif mediaTot == 1:
    print(B)
elif mediaTot > 1:
    print(C)



