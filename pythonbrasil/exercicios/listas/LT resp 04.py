vetor = []
consoantes = []
cons = 0
for i in range(1,11):
    letra = str(input("Digite a %iª letra: "%(i)))
    if letra not in ("a", "e", "i", "o", "u"):
        cons += 1
        consoantes.append(letra)

print("")
print("Consoantes: ", cons, " = ", consoantes)
print("")

    
    
