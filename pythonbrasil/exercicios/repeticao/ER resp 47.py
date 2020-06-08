'''
Em uma competição de ginástica, cada atleta recebe votos de sete jurados.
A melhor e a pior nota são eliminadas. A sua nota fica sendo a média dos
votos restantes. Você deve fazer um programa que receba o nome do ginasta
e as notas dos sete jurados alcançadas pelo atleta em sua apresentação e
depois informe a sua média, conforme a descrição acima informada (retirar
o melhor e o pior salto e depois calcular a média com as notas restantes).
As notas não são informados ordenadas. Um exemplo de saída do programa deve
ser conforme o exemplo abaixo:
    
Atleta: Aparecido Parente
Nota: 9.9
Nota: 7.5
Nota: 9.5
Nota: 8.5
Nota: 9.0
Nota: 8.5
Nota: 9.7

Resultado final:
Atleta: Aparecido Parente
Melhor nota: 9.9
Pior nota: 7.5
Média: 9,04
'''

print('-' * 35)
print('')
nome_atleta = str(input("Atleta: "))
print('')
while nome_atleta != "" or nome_atleta == 0:

    melhor_nota = 0
    pior_nota = 100
    media = 0

    for i in range(7):
        nota = float(input('Nota: '))
        media += nota
        
        if nota > melhor_nota:
            melhor_nota = nota

        if nota < pior_nota:
            pior_nota = nota


    print('')
    print('Resultado final:')
    print('Atleta: ', nome_atleta)
    print('Melhor salto: {:0.2f}m'.format(melhor_nota))
    print('Pior salto: {:0.2f}m'.format(pior_nota))
    print('Média dos demais saltos: {:0.2f}m'.format((media - (melhor_nota + pior_nota))/5))

    print('')
    print('-' * 35)

    print('')
    nome_atleta = str(input("Atleta: "))
    print('')
