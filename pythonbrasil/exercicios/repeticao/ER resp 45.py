'''
Desenvolver um programa para verificar a nota do aluno em uma prova com 10
questões, o programa deve perguntar ao aluno a resposta de cada questão e ao
final comparar com o gabarito da prova e assim calcular o total de acertos e
a nota (atribuir 1 ponto por resposta certa). Após cada aluno utilizar o
sistema deve ser feita uma pergunta se outro aluno vai utilizar o sistema.
Após todos os alunos terem respondido informar:

Maior e Menor Acerto;
Total de Alunos que utilizaram o sistema;
A Média das Notas da Turma.
Gabarito da Prova:

01 - A
02 - B
03 - C
04 - D
05 - E
06 - E
07 - D
08 - C
09 - B
10 - A

Após concluir isto você poderia incrementar o programa permitindo que o
professor digite o gabarito da prova antes dos alunos usarem o programa.
'''

proximo = 's'
gabarito = ['A','B','C','D','E','E','D','C','B','A']
final = []
alun = 0
maior = 0
menor = 10

print('-' * 30)

while proximo == 'S' or proximo == 's':

    print('\t   GABARITO')
    print('-' * 30)
    
    acertos = []
    acertos_n = []
    alunos = []
    resp = []
    
    nome = str(input('Nome: '))
    alunos.append(nome)
    alun += 1

    for i in range(len(gabarito)):
        respostas = str(input('Resposta da questão nº {} = '.format(i+1)))
        resp.append(respostas)

        if resp[i] == gabarito[i]:
            acertos_n.append(i+1)
            acertos.append(resp[i])

    final.append(alunos)
    final.append(acertos)

    print('-' * 30)

    print('Acertos:')
    print('')
    for i in range(len(acertos)):
        print('Questão nº {} - Letra {}'.format(acertos_n[i],acertos[i]))
    
    print(' ')

    for i in range(len(alunos)):
        print('\t ALUNO: {:>3s}'.format((alunos[i])))
        print('\t NOTA:  {:>5.2f}'.format(len(acertos)))
    
    print('-' * 30)
    print('')    
    proximo = str(input('Novo gabarito? [S - Sim] ou [N - Não]: '))
    print('')

    print('-' * 30)

media = 0
	
for i in range(1,len(final),2):
    if len(final[i]) > maior:
        maior = len(final[i])
    if len(final[i]) < menor:
        menor = len(final[i])

print('Maior acerto: ', maior)

print('Menor acerto: ', menor)

print('Total de alunos que utilizaram o sistema: ', alun)


for i in range(1,len(final),2):
    media += (len(final[i]))
	
print('A média das notas da turma: ', media / alun)




