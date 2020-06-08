'''
Faça um Programa que peça os 3 lados de um triângulo. O programa deverá
informar se os valores podem ser um triângulo. Indique, caso os lados
formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
Dicas:
Três lados formam um triângulo quando a soma de quaisquer dois lados
for maior que o terceiro;

Triângulo Equilátero: três lados iguais;
Triângulo Isósceles: quaisquer dois lados iguais;
Triângulo Escaleno: três lados diferentes;
'''

### ALGORITMO ###
a = int(input("Digite o lado A: "))
b = int(input("Digite o lado B: "))
c = int(input("Digite o lado C: "))

if a == b == c:
    print("Equilatero")
elif a == b != c or a != b == c or a == c != b:
    print("Isóceles")
elif a != b != c and a != c != b:
    print("Escaleno")
    
    
     
### FUNÇÃO ###
def triangulo(a,b,c):
    if a == b == c:
        print("Equilatero")
    elif a == b != c or a != b == c or a == c != b:
        print("Isóceles")
    elif a != b != c and a != c != b:
        print("Escaleno")
