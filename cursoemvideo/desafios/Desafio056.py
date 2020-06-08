'''
Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
No final do programa, mostre: a média de idade do grupo,
qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
'''

soma_idade = 0
contador_mulher = 0
idade_homem_velho = 0
homem_velho = ''
for i in range(1,5):
    print('----- {}ª PESSOA -----'.format(i))
    nome = str(input('Nome: '))
    
    idade = int(input('Idade: '))
    soma_idade += idade

    sexo = str(input('Sexo[M/F]: ')).strip()

    if i == 1 and sexo in 'Mm':
        homem_velho = nome
        idade_homem_velho = idade
    if sexo in 'Mm' and idade > idade_homem_velho:
        idade_homem_velho = idade
        homem_velho = nome
    if sexo in 'Ff' and idade < 20:
        contador_mulher += 1
        
media_idade = soma_idade / 4

print('')
  
print('A média de idade do grupo é de {} anos.'.format(media_idade))
print('O homem mais velho tem {} anos e se chama {}.'.format(idade_homem_velho, homem_velho))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(contador_mulher))
