fm = str(input("Digite o sexo - [M - Masculino] ou [F - Feminino]: "))

def foum():
    if fm == "M":
        print("M - Masculino")
    if fm == "F":
        print("F - Feminino")
    
    def si():
        while fm != "M" and fm != "F":
            print("Sexo inválido, tente novamente!")
            fm = str(input("Digite o sexo - [M - Masculino] ou [F - Feminino]: "))
            foum()
    si()
foum()
    
