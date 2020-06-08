'''
Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias
vezes e limitando o fatorial a números inteiros positivos e menores que 16.
'''



deNovo = "S"
while deNovo != "N":
    fat = 1
    print("****************** F A T O R I A L *************************")
    print("")
    n = int(input("\t\t Digite o fatorial: "))
    if n >= 0 and n < 16:
        for i in range(1, n+1):
            fat *= i
        print("")
        print("\t\t Fatorial de %i! é" %n, fat,)
        print("")
    else:
        print("")
        print("\t   Valor incorreto, tente novamente...")
        print("")
    print("************************************************************")
    print("")
    deNovo = str(input("Calcular novo Fatorial [S - Sim / N - Não]: "))
    print("")




##FATORIAL com While

'''
fat = 1
i = 1
while i < n+1:
    fat *= i
    i += 1
print(fat)
'''
