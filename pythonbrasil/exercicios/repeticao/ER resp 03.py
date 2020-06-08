#NOME
nome = str(input("NOME: "))
b = len(nome)
c = "abc"
d = len(c)

while b <= d:
    print("Nome errado, digite novamente!")
    nome = str(input("NOME: "))
    b = len(nome)
    c = "abc"
    d = len(c)

#IDADE
idade = int(input("IDADE: "))
while idade < 0 or idade > 150:
    if idade < 0:
        print("Você ainda é um espermatozoide, tente novamente na proxima transa!")
    else:
        idade > 150
        print("Parabéns sua múmia, tente novamente na proxima encarnação!")
    idade = int(input("IDADE: "))

#SALÁRIO
salario = float(input("SALÁRIO: R$ "))
while salario <= 0:
    print("Salário inválido, tente novamente")
    salario = float(input("SALÁRIO: R$ "))

#SEX0
sexo = str(input("SEXO [M/F]: "))
while sexo != "M" and sexo != "m" and sexo != "F" and sexo != "f":
    print("Escolha M = masculino ou F = feminino, tente novamente!")
    sexo = str(input("SEXO: "))

#ESTADO CIVIL
estciv = str(input("ESTADO CIVIL [S - Solteiro / C - Casado / V - Viúvo / D - Divorciado]: "))
while estciv != "S" and estciv != "s" and estciv != "C" and estciv != "c" and estciv != "V" and estciv != "v" and estciv != "D" and estciv != "d":
    print("Estado civil incorreto, tente novamente!")
    estciv = str(input("ESTADO CIVIL [S - Solteiro / C - Casado / V - Viúvo / D - Divorciado]: "))


#RESULTADO
print("")
print("")
print(" DADOS IMPRESSOS: ")
print("")
print("NOME: ", nome)
print("IDADE: ", idade)
print("SALÁRIO: R$ %2.2f" %salario)
print("SEXO: ", sexo)
print("ESTADO CIVIL: ", estciv)
    



    



    
