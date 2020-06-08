'''
Faça um programa que leia dez conjuntos de dois valores, o primeiro representando
o número do aluno e o segundo representando a sua altura em centímetros. Encontre
o aluno mais alto e o mais baixo. Mostre o número do aluno mais alto e o número do
aluno mais baixo, junto com suas alturas.
'''

quant_alunos = 10

cod_maisAlto = 0
cod_maisBaixo = 0

mais_alto = 0
mais_baixo = 5

for i in range(quant_alunos):

    print('')
    
    cod_aluno = int(input('Digite o número do aluno: '))
    altura = float(input('Altura: '))

    if altura > mais_alto:
        cod_maisAlto = cod_aluno
        mais_alto = altura

    if altura < mais_baixo:
        cod_maisBaixo = cod_aluno
        mais_baixo = altura

print('')

print('ALUNOS: ')
print('O aluno mais alto foi o nº %i com a altura de %0.2f'%(cod_maisAlto,mais_alto))
print('O aluno mais baixo foi o nº %i com a altura de %0.2f'%(cod_maisBaixo,mais_baixo))        


    



