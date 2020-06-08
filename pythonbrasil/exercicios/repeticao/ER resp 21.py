'''
Numa eleição existem três candidatos. Faça um programa que peça o número total
de eleitores. Peça para cada eleitor votar e ao final mostrar o número de votos
de cada candidato.
'''


                        ### ALGORITMO ###

votos = []
mais_votado = 0
maior_voto = []
maior_i = 0

print('\n')

print(70 * '*')
print(26 * '*', 'E L E I Ç Õ E S', 27 * '*')
print(70 * '*')

print('\n')

print('               ', '    VOTE EM UM DOS CANDIDATOS:')

print('')

print('(Candidato 1)', end = '               ')
print('(Candidato 2)', end = '               ')
print('(Candidato 3)')

print('\n')

eleitor = int(input('\t\t Digite o número total de eleitores: '))

print('\n')

for i in range(1,eleitor + 1):
    voto = int(input('\t\t\t Eleitor %i - Candidato: '%i))
    votos.append(voto)

for i in range(len(votos)):
    maior_voto.append(votos.count(i))
    if votos.count(i) > mais_votado:
        mais_votado = votos.count(i)
        maior_i = i


print('\n ')
print('\t O Candidato %i foi o mais votado com um total de %i votos.'%(maior_i, mais_votado))
print('')
print(70 * '*')
print(70 * '*')
print(70 * '*')


