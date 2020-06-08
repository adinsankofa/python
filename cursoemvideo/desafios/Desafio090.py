'''
Exercício Python 090: Faça um programa que leia nome e média de um aluno,
guardando também a situação em um dicionário. No final, mostre o conteúdo
da estrutura na tela.
'''

# VERSÃO GUANABARA:
aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['nota'] = float(input(f'Média de {aluno["nome"]}: '))

if aluno['nota'] >= 7:
    aluno['situacao'] = 'Aprovado'
elif 5 <=  aluno['nota'] <7:
    aluno['situacao'] = 'Recuperação'
else:
    aluno['situacao'] = 'Reprovado';

print('-=' * 30)
for k, v in aluno.items():
    print(f' - {k} é igual a {v}')
    
    

# VERSÃO BRUNO:

boletim = dict()
boletim['nome'] = str(input('Nome: '))
boletim['nota'] = float(input(f'Média de {boletim["nome"]}: '))

if boletim['nota'] < 6:
    boletim['situacao'] = 'Reprovado'
elif boletim['nota'] >= 6 and boletim['nota'] < 7:
    boletim['situacao'] = 'Recuperação'
else:
    boletim['situacao'] = 'Aprovado';

print('-=' * 30)

print(f' - nome é igual a {boletim["nome"]} ')
print(f' - media é igual a {boletim["nota"]} ')
print(f' - situação é igual a {boletim["situacao"]}' )
