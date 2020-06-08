'''
Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias
pessoas, guardando os dados de cada pessoa em um dicionário e todos os
dicionários em uma lista. No final, mostre: A) Quantas pessoas foram
cadastradas
'''

#VERSÃO GUANABARA
galera = list()
pessoa = dict()
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print ('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break
print('-=' * 30)
print(f'A) Ao todo temos {len(galera)} pessoas cadastradas')
media = soma / len(galera)
print(f'B) A média de idade é de {media : 0.2f} anos.')
print(f'C) As mulheres cadastradas foram: ', end=' ')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]} ', end='')
print()
print(f'D) Lista de pessoas que estão acima da média: ', end='')
for p in galera:
    if p['idade'] >= media:
        print('     ')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
print('<< ENCERRADO >>')
        
        
    


#VERSÃO BRUNO
pessoas = list()
sexo = ""
continua = 'S'
while continua != 'N':
    nomes = dict()
    nomes['nome'] = str(input('Nome: '))
    while True:
        sexo = str(input('Sexo [M/F]: ')).strip().upper()
        if sexo == 'M' or sexo == 'F':
            break
        else:
            print('ERRO! Por favor, digite apenas M ou F.')
    nomes['sexo'] = sexo
    nomes['idade'] = int(input('Idade: '))
    while True:
        continua = str(input('Quer continuar? [S/N] ')).strip().upper()
        if continua == 'S' or continua == 'N':
            break
        else:
            print('ERRO! Por favor, digite apenas S ou N.')
    if continua == 'S':
        print('-' * 30)
    else:
        print('-=' * 30)
    pessoas.append(nomes)
print(f'A) Ao todo temos {len(pessoas)} pessoas cadastradas')
media = 0
for i in range(len(pessoas)):
    media += pessoas[i]['idade'] / len(pessoas)
maiormedia = list()
mulheres = list()
for i in range(len(pessoas)):
    if pessoas[i]['idade'] > media:
        maiormedia.append(pessoas[i])
    else:
        pass
    if pessoas[i]['sexo'] == 'F':
        mulheres.append(pessoas[i]['nome'])
    else:
        pass
print(f'B) A média de idade é de {media : 0.2f} anos.')		
print(f'C) As mulheres cadastradas foram: ', end=' ')
for i in mulheres:
    print(f'{i} ', end=' ')
print('')
print(f'D) Lista de pessoas que estão acima da média: ', end='')
for i in range(len(maiormedia)):
    print('')
    for k, v in maiormedia[i].items():
        print(f'\t {k} = {v}', end='; ')
print('')
print('<< ENCERRADO >>')

    


