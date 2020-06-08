'''
Faça um Programa para leitura de três notas parciais de um aluno. O programa deve
calcular a média alcançada por aluno e presentar: A mensagem "Aprovado", se a média
for maior ou igual a 7, com a respectiva média alcançada; A mensagem "Reprovado",
se a média for menor do que 7, com a respectiva média alcançada; A mensagem "Aprovado
com Distinção", se a média for igual a 10.
'''

                    ### ALGORITMO ###

print('***************************************************')
print('***************** BOLETIM ESCOLAR *****************')
print('***************************************************')
print('')
notas = 0
for i in range(1,4):
    notas += float(input('\t\t Digite a %iª nota: '%i))
media = notas / 3
print('')

if 7 <= media < 10:
    status = 'Aprovado'
if media < 7:
    status = 'Reprovado'
if media == 10:
    status = 'Aprovado com Distinção'
    
print('***************************************************')
print('A média foi %0.2f, aluno %s.'%(media, status))
print('***************************************************')





                    ### FUNÇÃO ###

def Boletim(nota_1,nota_2,nota_3):

    media = (nota_1 + nota_2 + nota_3) / 3

    status = 0
    
    if 7 <= media < 10:
        status = 'Aprovado'
    if media < 7:
        status = 'Reprovado'
    if media == 10:
        status = 'Aprovado com Distinção'
    
    return print('A média foi %0.2f, aluno %s.'%(media, status))

