'''
Faça um programa que peça para n pessoas a sua idade, ao final o programa deverá
verificar se a média de idade da turma varia entre 0 e 25,26 e 60 e maior que 60;
e então, dizer se a turma é jovem, adulta ou idosa, conforme a média calculada.
'''

print('\n')

soma = 0
n = int(input('Digite o número de pessoas: '))

print('')

for i in range(1,n+1):
    idade = int(input('Idade: '))
    soma += idade
media_idade = soma / n

print('')

if 0 < media_idade <= 25:
    print('A maioria é de JOVENS pois a idade média é %i anos.'%(media_idade))
elif 26 <= media_idade <= 60:
    print('A maioria é de ADULTOS pois a idade média é %i anos.'%media_idade)
elif media_idade > 60:
    print('A maioria é de IDOSOS pois a idade média é %i anos.'%media_idade)

print('\n')    

