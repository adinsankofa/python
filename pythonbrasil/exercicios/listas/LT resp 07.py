soma = 0
multi = 1
numeros = []

for i in range(1,6):
    
    num = int(input("Digite o %iº número: "%(i)))

    soma += num
    multi *= num

    numeros.append(num)

print("")
print("Soma: ", soma)
print("Multiplicação: ", multi)
print("Números digitados: ", numeros)
print("")    
