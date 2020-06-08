"""
Faça um Programa que leia três números e mostre-os em ordem decrescente
"""

a = int(input("A: "))
b = int(input("B: "))
c = int(input("C: "))

if a > b and b > c:
    print("Decrescente: ", a, b, c)

if b > a and a > c:
    print("Decrescente: ", b, a, c)
    
if c > b and b > a:
    print("Decrescente: ", c, b, a)





        
    
