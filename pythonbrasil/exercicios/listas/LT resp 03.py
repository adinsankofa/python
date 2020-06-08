notas = []
media = 0
somaN = 0
for i in range(1,5):
    n = float(input("Digite a %iª nota: "%(i)))
    notas.append(n)
    somaN += n

media = somaN / 4

print("Notas: ", notas)
print("Média: %2.2f " %media)
