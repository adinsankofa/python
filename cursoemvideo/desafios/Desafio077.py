'''
Exercício Python 077: Crie um programa que tenha uma tupla com várias palavras
(não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais
são as suas vogais.
'''


## VERSÃO GUANABARA:
palavras = ("aprender",
            "programar",
            "linguagem",
            "python",
            "curso",
            "gratis",
            "estudar",
            "praticar",
            "trabalhar",
            "mercado",
            "programador",
            "futuro")

for p in palavras:
    print(f"\nNa palavra {p.upper()} temos ", end="")
    for letra in p:
        if letra.lower() in "aeiou":
            print(letra, end=" ")
        else:
            pass



## VERSÃO BRUNO:
palavras = ("APRENDER",
            "PROGRAMAR",
            "LINGUAGEM",
            "PYTHON",
            "CURSO",
            "GRATIS",
            "ESTUDAR",
            "PRATICAR",
            "TRABALHAR",
            "MERCADO",
            "PROGRAMADOR",
            "FUTURO")

for i in range(len(palavras)):
    print(f"Na palavra {palavras[i]} temos ", end="")
    for y in palavras[i]:
        if y in "AEIOU":
            print(y.lower(), end=" ")
        else:
            pass
    print("")
       
        
            

