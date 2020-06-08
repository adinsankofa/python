'''
Uma academia deseja fazer um senso entre seus clientes para descobrir
o mais alto, o mais baixo, a mais gordo e o mais magro, para isto você
deve fazer um programa que pergunte a cada um dos clientes da academia
seu código, sua altura e seu peso. O final da digitação de dados deve
ser dada quando o usuário digitar 0 (zero) no campo código. Ao encerrar
o programa também deve ser informados os códigos e valores do clente mais
alto, do mais baixo, do mais gordo e do mais magro, além da média das
alturas e dos pesos dos clientes
'''

print('************************************************')
print('******************* ACADEMIA *******************')
print('***************** JOÃO MAROMBA *****************')
print('************************************************')

print('')

codigo = 1
mais_alto = 0
mais_gordo = 0

while codigo != 0:
    codigo = int(input('Código: '))
    if codigo > 0:
        altura = float(input('Altura: '))
        peso = float(input('Peso: '))

    print('')

    if altura > mais_alto:
        cod_maisAlto = codigo
        mais_alto = altura

    if peso > mais_gordo:
        cod_maisGordo = codigo
        mais_gordo = peso

print('')

print('************************************************')
print('************ R E S U L T A D O: ****************')
print('************************************************')

print('')

print('ALTURA:')
print('-' * 8)
print('Código: ', cod_maisAlto)
print('Aluno mais alto: %0.2fm'%mais_alto)

print('')
print('')

print('PESO:')
print('-' * 8)
print('Código: ', cod_maisGordo)
print('Aluno mais gordo: %0.2fkg'%mais_gordo)

print('')

print('************************************************')
print('************************************************')
print('************************************************')
print('************************************************')
