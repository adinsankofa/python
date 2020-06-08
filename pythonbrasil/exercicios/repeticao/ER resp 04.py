
a = 80000
b = 200000
quant = 0

while a < b:

    soma_A = (a / 100) * 3.0
    a += soma_A

    soma_B = (b / 100) * 1.5
    b += soma_B

    if a < b:
        quant += 1

    print("População A: %i " %a)
    print("População B: %i " %b)
    print("")
print("Anos: ", quant)
print("")
