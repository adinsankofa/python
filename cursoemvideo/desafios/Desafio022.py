'''
Crie um programa que leia o nome completo de uma pessoa e mostre:
O nome com todas as letras maíusculas e minusculas.
Quantas letras ao todo (sem considerar espaços).
Quantas letras tem o primeiro nome.
'''

nome = str(input('Digite o nome completo: ')).strip()

print('O nome com todas as letras maíusculas: ', nome.upper())
print('O nome com todas as letras minusculas: ', nome.lower())
print('Quantas letras ao todo (sem considerar espaços): {}'.format(len(nome) - nome.count(' ')))

#print('Quantas letras tem o primeiro nome: ', nome.find(' '))
separa = nome.split()
print('O primeiro nome é {} e tem {} letras.'.format(separa[0], len(separa[0])))


