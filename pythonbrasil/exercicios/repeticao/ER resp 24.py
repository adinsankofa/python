'''
Faça um programa que calcule o mostre a média aritmética de N notas.
'''

n = int(input('Digite o número de notas: '))

print('')

soma = 0
for i in range(1, n+1):
    nota = float(input('Nota %i: '%i))
    soma += nota

print('')

print('A média das notas é %0.2f'%(soma / n))
