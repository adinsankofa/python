'''
Faça um programa que leia um número indeterminado de valores, correspondentes a notas,
encerrando a entrada de dados quando for informado um valor igual a -1
(que não deve ser armazenado). Após esta entrada de dados, faça:
Mostre a quantidade de valores que foram lidos;
Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
Calcule e mostre a soma dos valores;
Calcule e mostre a média dos valores;
Calcule e mostre a quantidade de valores acima da média calculada;
Calcule e mostre a quantidade de valores abaixo de sete;
Encerre o programa com uma mensagem;
'''

print("")

print("                                     VÁRIAS VARIÁVEIS")

print("")


menor7 = []
unicosM7 = []
notas = []
nota = 0

while nota != -1:
    nota = float(input("Nota: "))
    if nota != -1:
        notas.append(nota)

print("")
print("Quantidade de valores lidos: %i"%len(notas))

print("")
print("Valores lado a lado: ", notas)

print("")
print("Valores em ordem inversa: ")
for i in (notas[::-1]):
    print("%2.1f"%i)

print("")
print("Soma dos valores: %2.2f"%sum(notas))

print("")
print("Média dos valores: %0.2f"%(sum(notas)/len(notas)))

print("")
print("Valores acima da média calculada: ")
for i in notas:
    if i > sum(notas)/len(notas):
        print("%2.2f"%i, end = "   ")

print("")
print("")
for i in notas:
    if i < 7:
        menor7.append(i)

unicosM7 = list(set(menor7))

print("Valores abaixo de 7: ", unicosM7)        

print("")
print("")
print("")
print("                                     PYTHON agradece!")

