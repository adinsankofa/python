'''
Exercício Python 072: Crie um programa que tenha uma dupla totalmente preenchida
com uma contagem por extenso, de zero até vinte. Seu programa deverá ler um número
pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
'''

num_extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis',
               'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze',
               'quartoze', 'quinze', 'dezesseis', 'dezessete', 'dezoito',
               'dezenove', 'vinte')

while True:
    num = int(input("Digite um número entre 0 e 20: "))
    if 0 <= num <= 20:
        break
    print('Tente novamente. ', end='')
    
print(f'Voce digitou o número {num_extenso[num]}')
