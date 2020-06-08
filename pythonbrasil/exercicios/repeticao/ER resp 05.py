continua = "S"

while continua == "S":

    print("")

    a = int(input("Digite a população do país A: "))
    b = int(input("Digite a população do país B: "))

    taxa_A = float(input("Taxa de crescimento de A: "))
    taxa_B = float(input("Taxa de crescimento de B: "))

    quantA = 0
    quantB = 0

    if a < b:

        while a < b:

            soma_A = (a / 100) * taxa_A
            a += soma_A

            soma_B = (b / 100) * taxa_B
            b += soma_B

            if a < b:
                quantA += 1
            
        print("Anos para o Alcance - A: %i" %quantA)

    elif b < a:

        while b < a:

            soma_A = (a / 100) * taxa_A
            a += soma_A

            soma_B = (b / 100) * taxa_B
            b += soma_B

            if b < a:
                quantB += 1
            
        print("Anos para o Alcance - B: %i" %quantB)

    print("")

    continua = str(input("Quer continuar o teste? [N - Não] ou [S - Sim]: "))

