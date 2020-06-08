'''
Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação
da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como
"Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado
como "Inocente".
'''


resp = 0

nome = input('Nome: ')

telefonou = input("Telefonou para a vítima? = ")
if telefonou == 'S' or telefonou == 's':
    resp += 1
    
esteve = input("Esteve no local do crime? = ")
if esteve == 'S' or esteve == 's':
    resp += 1
    
mora = input("Mora perto da vítima? = ")
if mora == 'S' or mora == 's':
    resp += 1

devia = input("Devia para a vítima? = ")
if devia == 'S' or devia == 's':
    resp += 1
    
trabalhou = input("Já trabalhou com a vítima? = ")
if trabalhou == 'S' or trabalhou == 's':
    resp += 1

print('\n')

print('RESULTADO')
print('-' * 10)

if resp == 2:
    print(f'{nome} é SUSPEITO.')
elif 2 < resp <= 4:
    print(f'{nome} é CÚMPLICE.')
elif resp == 5:
    print(f'{nome} é ASSASSINO.')
else:
    print(f'{nome} é INOCENTE.')



