lista_invertida = []

for i in range(1,11):
    num = int(input("Digite o %i número: " %(i)))
    lista_invertida.append(num)

lista_invertida.reverse()

print(lista_invertida)
