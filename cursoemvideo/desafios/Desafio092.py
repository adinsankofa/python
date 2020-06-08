'''
Exercício Python 092: Crie um programa que leia nome, ano de nascimento
e carteira de trabalho e cadastre-o (com idade) em um dicionário. Se por
acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de
contratação e o salário. Calcule e acrescente, além da idade, com quantos
anos a pessoa vai se aposentar.
'''


# VERSÃO GUANABARA:
from datetime import datetime
dados = dict()
dados['nome'] = str(input('Nome: '))
nasc = int(input('Ano de Nascimento: '))
dados['idade'] = datetime.now().year - nasc
dados['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if dados['ctps'] != 0:
    dados['ano_contratacao'] = int(input('Ano de Contratação: '))
    dados['salario'] = float(input('Salário: R$ '))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratacao'] + 35) - datetime.now().year)
    print('-=' * 30)
for k, v in dados.items():
    print(f' = {k} tem o valor {v}')



# VERSÃO BRUNO:
cadastro = dict()
cadastro['nome'] = str(input('Nome: '))
cadastro['ano_nascimento'] = int(input('Ano de Nascimento: '))
cadastro['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if cadastro['ctps'] != 0:
    cadastro['ano_contratacao'] = int(input('Ano de Contratação: '))
    cadastro['salario'] = float(input('Salário: R$ '))
    print('-=' * 30)
    idade = datetime.now().year - cadastro['ano_nascimento']
    aposentadoria = ((idade + cadastro['ano_contratacao'] + 35)) - datetime.now().year
    print(f"- nome tem o valor: {cadastro['nome']}")
    print(f"- idade tem o valor: {idade}")
    print(f"- ctps tem o valor: {cadastro['ctps']}")
    print(f"- contratação tem o valor: {cadastro['ano_contratacao']}")
    print(f"- salário tem o valor: R${cadastro['salario'] : 0.2f}")
    print(f"- aposentadoria tem o valor: {aposentadoria}")
else:
    print('-=' * 30)
    print(f"- nome tem o valor: {cadastro['nome']}")
    print(f"- idade tem o valor: {cadastro['ano_nascimento']}")
    print(f"- ctps tem o valor: {cadastro['ctps']}")
                       

        



    
    
    
