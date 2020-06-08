'''
Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores.
Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.
'''

cand1, cand2, cand3 = 0,0,0

print('******************************************************')
print('********************** ELEIÇÕES **********************')
print('******************************************************')

print('\n')

eleitores = int(input('\tDigite o número total de eleitores: '))

print('')

for i in range(eleitores):
    voto = int(input('\t    Vote nos candidatos(1,2,3):'))

    if voto == 1:
        cand1 += 1

    if voto == 2:
        cand2 += 1

    if voto == 3:
        cand3 += 1

print('\n')

print('\t\t   TOTAL DE VOTOS:')

print('\t\t   Candidato 1: ',cand1)
print('\t\t   Candidato 2: ',cand2)
print('\t\t   Candidato 3: ',cand3)

print('\n')
        
    
print('******************************************************')
print('******************************************************')
print('******************************************************')



                
