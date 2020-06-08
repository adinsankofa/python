"""
Faça um Programa que pergunte em que turno você estuda.
Peça para digitar M-matutino ou V-Vespertino ou N- Noturno.
Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!
, conforme o caso.
"""

turno = str(input("Em qual turno você estuda? "))

if turno == "M":
        print("BOM DIA!")
elif turno == "V":
        print("BOA TARDE!")
elif turno == "N":
        print("BOA NOITE!")

while turno != "M" and turno != "V" and turno != "N":
 
        if turno != "M" and turno != "V" and turno != "N":
            print("Valor inválido!")

        turno = str(input("Em qual turno você estuda? "))

        if turno == "M":
            print("BOM DIA!")
        elif turno == "V":
            print("BOA TARDE!")
        elif turno == "N":
            print("BOA NOITE!")


   
        
