'''
Exercício Python 097: Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer
como parâmetro e mostre uma mensagem com tamanho adaptável.
'''


#VERSÃO GUANABARA
def escreva(msg):
    tam = len(msg) + 4
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)



#VERSÃO GUANABARA
def ajusta():
    palavra = str(input("Digite uma palavra: "))
    num_letras = len(palavra)
    print("\n")
    print("~" * num_letras)
    print(palavra)
    print("~" * num_letras)

