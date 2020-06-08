def vc():
    vouc = str(input("Digite uma letra: "))

    if vouc not in ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U"):
        print("Letra %s: CONSOANTE" %vouc)
    else:
        print("Letra %s: VOGAL" %vouc)

vc()
