'''
Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120. A saída deve ser conforme o exemplo abaixo:
Fatorial de: 5
5! =  5 . 4 . 3 . 2 . 1 = 120
'''


        ### FATORIAL com FOR ###

n = 5
fat = 1
print('Fatorial de: %i'%n)
print('%i!  =  '%n, end = '')
for i in range(n,1,-1):
    fat = fat * i
    print(i, end = ' . ')
print('1  =  ', end = '')
print(fat)




        ### FATORIAL com WHILE ###

n = 5
i = 1
fat = 1
print('Fatorial de: %i'%n)
print('%i!  = '%n,'%i . '%n, end = '')
while i < n+1:
    if n-i > 1:
        print(n - i, end = ' . ')
    fat = fat * i
    i += 1 

print('1  =  ', end = '')
print(fat)
    

    


             ### FUNÇÃO ###

def fatorial(n):
    fat = 1
    print('Fatorial de: %i'%n)
    print('%i!  =  '%n, end = '')
    for i in range(n,1,-1):
        fat = fat * i
        print(i, end = ' . ')
    print('1  =  ', end = '')
    print(fat)
