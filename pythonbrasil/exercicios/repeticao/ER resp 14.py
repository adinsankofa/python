num = int(input("Digite quantos números você quer: "))

par = []
impar = []
par1 = 0
impar1 = 0

for i in range(1,num+1):

    if i % 2 == 0:
        par1 += 1
        par.append(i)

    if i % 2 == 1:
        impar1 += 1
        impar.append(i)


print("PARES: %i" %par1, "=", par)
print("IMPAR: %i" %impar1, "=", impar)



    
    
