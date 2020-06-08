'''
Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito. Foram obtidos os seguintes dados:
Código da cidade;
Número de veículos de passeio (em 1999);
Número de acidentes de trânsito com vítimas (em 1999). Deseja-se saber:
Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
Qual a média de veículos nas cinco cidades juntas;
Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos
de passeio.
'''

cod_maior = 0
maior_ind_acidentes = 0
cod_menor = 0
menor_ind_acidentes = 1000000
media_menosde2000 = 0
veic_passeio = 0
veiculos = 0

for i in range(1,6):

    print('')

    cod = int(input('Código da cidade: '))
    veic_passeio = int(input('Número de veículos de passeio (2017): '))
    if veic_passeio < 2000:
        media_menosde2000 += veic_passeio

    veiculos += veic_passeio
    
    acidentes = int(input('Número de acidentes com vitimas: '))

    if acidentes > maior_ind_acidentes:
        cod_maior = cod
        maior_ind_acidentes = acidentes

    if acidentes < menor_ind_acidentes:
        cod_menor = cod
        menor_ind_acidentes = acidentes

    
print('\n')                    

print('MÉDIA DE VEÍCULOS: %0.2f'%(veiculos / 5))
print('O MENOR índice de acidentes ocorreu na cidade de código nº %i com %i acidentes.'%(cod_menor, menor_ind_acidentes))
print('O MAIOR índice de acidentes ocorreu na cidade de código nº %i com %i acidentes.'%(cod_maior, maior_ind_acidentes))
print('MÉDIA (menos de 2000 habitantes): ', media_menosde2000)

print('\n')
