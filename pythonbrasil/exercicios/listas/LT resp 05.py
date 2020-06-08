def pareimpar():
    par = []
    impar = []
    for i in range(1, 21):
        num = int(input("Digite o %iº número: " %(i)))
        if num % 2 == 0:
            par.append(num)
        if num % 2 == 1:
            impar.append(num)
    print("")
    print("PARES: ", par)
    print("IMPARES: ", impar)

pareimpar()
    
    
