'''
Em uma competição de salto em distância cada atleta tem direito a cinco saltos.
No final da série de saltos de cada atleta, o melhor e o pior resultados são
eliminados. O seu resultado fica sendo a média dos três valores restantes.
Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas
pelo atleta em seus saltos e depois informe a média dos saltos conforme a
descrição acima informada (retirar o melhor e o pior salto e depois calcular a
média). Faça uso de uma lista para armazenar os saltos. Os saltos são informados
na ordem da execução, portanto não são ordenados. O programa deve ser encerrado
quando não for informado o nome do atleta. A saída do programa deve ser conforme
o exemplo abaixo:
    
Atleta: Rodrigo Curvêllo

Primeiro Salto: 6.5 m
Segundo Salto: 6.1 m
Terceiro Salto: 6.2 m
Quarto Salto: 5.4 m
Quinto Salto: 5.3 m

Melhor salto:  6.5 m
Pior salto: 5.3 m
Média dos demais saltos: 5.9 m

Resultado final:
Rodrigo Curvêllo: 5.9 m

'''

ordem_saltos = ['Primeiro', 'Segundo', 'Terceiro', 'Quarto', 'Quinto']

print('-' * 35)
print('')
nome_atleta = str(input("Atleta: "))
print('')
while nome_atleta != "" or nome_atleta == 0:
    melhor_salto = 0
    pior_salto = 100
    media_saltos = 0
    saltos = 0
    for i in ordem_saltos:
        saltos = float(input('{:s} Salto: '.format(i)))
        media_saltos += saltos
        
        if saltos > melhor_salto:
            melhor_salto = saltos

        if saltos < pior_salto:
            pior_salto = saltos

    print('')
    print('Melhor salto: {:0.2f}m'.format(melhor_salto))
    print('Pior salto: {:0.2f}m'.format(pior_salto))
    print('Média dos demais saltos: {:0.2f}m'.format((media_saltos - (melhor_salto + pior_salto))/3))

    print('')

    print('Resultado final:')
    print('{}: {:0.2f}'.format(nome_atleta, (media_saltos - (melhor_salto + pior_salto))/3))

    print('-' * 35)

    print('')
    nome_atleta = str(input("Atleta: "))
    print('')
    
    
    
    
    
    
