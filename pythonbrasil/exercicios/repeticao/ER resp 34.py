'''
Os números primos possuem várias aplicações dentro da Computação, por exemplo
na Criptografia. Um número primo é aquele que é divisível apenas por um e por
ele mesmo. Faça um programa que peça um número inteiro e determine se ele é ou
não um número primo.
'''

                            ### ALGORITMO ###

num = int(input('Digite um número: '))
div = []
for i in range(1,num+1):
    if num % i == 0:
        div.append(i)

if len(div) == 2:
    print('O número', num, 'É PRIMO pois é divisivel apenas por', div)
else:
    print('O número', num, 'NÃO É PRIMO pois é divisivel por', div)




                            ### FUNÇÃO ###

def primo(num):
    div = []
    for i in range(1,num+1):
        if num % i == 0:
            div.append(i)

    if len(div) == 2:
        print('O número', num, 'É PRIMO pois é divisivel apenas por', div)
    else:
        print('O número', num, 'NÃO É PRIMO pois é divisivel por', div)


    
