'''
Em uma eleição presidencial existem quatro candidatos. Os votos são informados
por meio de código. Os códigos utilizados são:
1 , 2, 3, 4  - Votos para os respectivos candidatos 
(você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
5 - Voto Nulo
6 - Voto em Branco
Faça um programa que calcule e mostre:
O total de votos para cada candidato;
O total de votos nulos;
O total de votos em branco;
A percentagem de votos nulos sobre o total de votos;
A percentagem de votos em branco sobre o total de votos. Para finalizar o
conjunto de votos tem-se o valor zero.
'''

cand1 = ''
cand2 = ''
cand3 = ''
cand4 = ''
nulo = ''
brancos = ''
  
votosCand1 = 0
votosCand2 = 0
votosCand3 = 0
votosCand4 = 0
votosNulo = 0
votosBranco = 0

votosTot = 0

print('*' * 55)
print('*' * 55)
print('*' * 55)

print('\n')

print('{:^50.50s}'.format('   CANDIDATOS: '))
print('\t\t ','-' * 14)
print('')
print('\t\t 1 - José Carrapicho')
print('\t\t 2 - Carlos Caolho')
print('\t\t 3 - Maria Mão Leve')
print('\t\t 4 - Bruna Carreirão')

voto = 1

print('')
while voto != 0:

    if voto > 6:
        print('')
        print('Voto incorreto, digite novamente!')
        print('')
        
    voto = int(input('Digite o candidato (0 - Sair / 5 - Nulo / 6 - Branco): '))

    if voto == 1:
        cand1 = 'José Carrapicho'
        votosCand1 += 1
        votosTot += 1

    if voto == 2:
        cand2 = 'Carlos Caolho'
        votosCand2 += 1
        votosTot += 1
        
    if voto == 3:
        cand3 = 'Maria Mão Leve'
        votosCand3 += 1
        votosTot += 1

    if voto == 4:
        cand4 = 'Bruna Carreirão'
        votosCand4 += 1
        votosTot += 1

    if voto == 5:
        nulo = 'Nulos'
        votosNulo += 1
        votosTot += 1

    if voto == 6:
        brancos = 'Brancos'
        votosBranco += 1
        votosTot += 1
    
     
print('\n')
 
print('{:^50.50s}'.format('  RESULTADO:'))
print('\t\t   ','-' * 12)

print('\t\t Total de Votos:  {:<17}'.format(votosTot))
if votosNulo > 0:
    print('\t\t Porcentagem de Nulos:  {:>5.2f}%'.format(votosNulo/ votosTot * 100))
if votosBranco > 0:
    print('\t\t Porcentagem de Brancos:  {:>5.2f}%'.format(votosBranco/ votosTot * 100))
    
print('')
print('\t CANDIDATOS', '\t\t VOTOS')

if votosCand1 > 0:
    print('\t {:<20} \t {:>3}'.format(cand1, votosCand1))
if votosCand2 > 0: 
    print('\t {:<20} \t {:>3}'.format(cand2, votosCand2))
if votosCand3 > 0:
    print('\t {:<20} \t {:>3}'.format(cand3, votosCand3))
if votosCand4 > 0:
    print('\t {:<20} \t {:>3}'.format(cand4, votosCand4))
if votosNulo > 0:
    print('\t {:<20} \t {:>3}'.format(nulo, votosNulo))
if votosBranco > 0:
    print('\t {:<20} \t {:>3}'.format(brancos, votosBranco))

print('\n')

print('*' * 55)
print('*' * 55)
print('*' * 55)
