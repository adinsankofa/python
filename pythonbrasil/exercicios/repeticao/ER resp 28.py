'''
Faça um programa que calcule o valor total investido por um colecionador em
sua coleção de CDs e o valor médio gasto em cada um deles. O usuário deverá
informar a quantidade de CDs e o valor para em cada um.
'''

CDs = int(input("Digite a quantidade de CD's: "))

print('')

n = 0
for i in range(1,CDs + 1):
   n += float(input('Valor do %iº CD: R$ '%i))

print('')
print("Valor total dos CD's: R$ %0.2f"%n)
print('')
print("Valor médio gasto por CD: R$ %0.2f"%(n / CDs))

    



