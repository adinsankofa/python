'''
Faça um programa que leia a largura e a altura de uma parede em metros,
calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo
que cada litro de tinta pinta uma área de 2m²
'''

altura = float(input('Digite a altura: '))
comprimento = float(input('Digite a largura: '))

area = altura * comprimento

print("Tinta: {:0.2f}m".format(area / 2))
