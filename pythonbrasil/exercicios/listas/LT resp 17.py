'''
Em uma competição de salto em distância cada atleta tem direito a cinco
saltos. O resultado do atleta será determinado pela média dos cinco valores
restantes. Você deve fazer um programa que receba o nome e as cinco distâncias
alcançadas pelo atleta em seus saltos e depois informe o nome, os saltos
e a média dos saltos. O programa deve ser encerrado quando não for informado
o nome do atleta. A saída do programa deve ser conforme o exemplo abaixo:

Atleta: Rodrigo Curvêllo
 
Primeiro Salto: 6.5 m
Segundo Salto: 6.1 m
Terceiro Salto: 6.2 m
Quarto Salto: 5.4 m
Quinto Salto: 5.3 m

Resultado final:
Atleta: Rodrigo Curvêllo
Saltos: 6.5 - 6.1 - 6.2 - 5.4 - 5.3
Média dos saltos: 5.9 m
'''

nomeAtleta = []
saltos = []
saltos1 = []
atleta = 0
while atleta != '':
    print("----------------------------------------------")
    atleta = str(input("Nome do Atleta: "))
    nomeAtleta.append(atleta)
    print("")

    saltos = ["Primeiro", "Segundo", "Terceiro", "Quarto", "Quinto"]

    if atleta != '':
        pulos = []
        for i in saltos:
            salto = float(input("%s Salto: "%(i)))
            pulos.append(salto)
        saltos1.append(pulos)
    
print("**********************************************")
print("******** R E S U L T A D O  F I N A L ********")
print("**********************************************")
for i in range(len(saltos1)):
    print("")
    print("Atleta: ", (nomeAtleta[i]))
    print("Saltos: ", saltos1[i])
    print("Média dos saltos: ", sum(saltos1[i])/5)
print("**********************************************")
    
    

            
            
            


        
