'''
Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice"
e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".
'''

r = "S"

perguntas = ["1) Telefonou para a vítima? [S / N] ", "2) Esteve no local do crime? [S / N] ", "3) Mora perto da vítima? [S / N] ",
"4) Devia para a vítima? [S / N] ", "5) Já trabalhou com a vítima? [S / N] "]

respostas = []

while r == "S":

    respostas = []
    somaSim = 0
    a = 0
    
    print("------------------------------------------------------------------------------")
    nome = str(input("NOME DO SUSPEITO: "))

    print("")
    print("QUESTIONÁRIO: ")

    for i in range(len(perguntas)):
        resp = str(input(perguntas[i]))
        respostas.append(resp)

    for i in respostas:
        if i == "S" or i == "s":
            somaSim += 1

    print("")

    if somaSim == 0 or somaSim == 1:
        print("Status de %s: INOCENTE"%nome)
    else:
        if somaSim == 2:
            print("Status de %s: SUSPEITO"%nome)
        else:
            if somaSim == 3 or somaSim == 4:
                print("Status de %s: CÚMPLICE"%nome)
            else:
                if somaSim == 5:
                    print("Status de %s: ASSASSINO"%nome)

    print("------------------------------------------------------------------------------")
    
    r = str(input("Entrevistar outro suspeito? [S / N] "))

    while r != "N" and r != "S":
        r = str(input("Entrevistar outro suspeito? [S / N] "))
    
    



  
