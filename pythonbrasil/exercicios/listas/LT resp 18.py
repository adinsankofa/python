'''
Uma grande emissora de televisão quer fazer uma enquete entre os seus telespectadores para
saber qual o melhor jogador após cada jogo. Para isto, faz-se necessário o desenvolvimento
de um programa, que será utilizado pelas telefonistas, para a computação dos votos. Sua equipe
foi contratada para desenvolver este programa, utilizando a linguagem de programação C++. Para
computar cada voto, a telefonista digitará um número, entre 1 e 23, correspondente ao número da
camisa do jogador. Um número de jogador igual zero, indica que a votação foi encerrada. Se um
número inválido for digitado, o programa deve ignorá-lo, mostrando uma breve mensagem de aviso,
e voltando a pedir outro número. Após o final da votação, o programa deverá exibir:
    
O total de votos computados;
Os númeos e respectivos votos de todos os jogadores que receberam votos;
O percentual de votos de cada um destes jogadores;
O número do jogador escolhido como o melhor jogador da partida, juntamente com o número de votos
e o percentual de votos dados a ele.

Observe que os votos inválidos e o zero final não devem ser computados como votos. O resultado
aparece ordenado pelo número do jogador. O programa deve fazer uso de arrays. O programa deverá
executar o cálculo do percentual de cada jogador através de uma função. Esta função receberá dois
parâmetros: o número de votos de um jogador e o total de votos. A função calculará o percentual e
retornará o valor calculado. Abaixo segue uma tela de exemplo. O disposição das informações deve
ser o mais próxima possível ao exemplo. Os dados são fictícios e podem mudar a cada execução do
programa. Ao final, o programa deve ainda gravar os dados referentes ao resultado da votação em
um arquivo texto no disco, obedecendo a mesma disposição apresentada na tela.
Enquete: Quem foi o melhor jogador?

Número do jogador (0=fim): 9
Número do jogador (0=fim): 10
Número do jogador (0=fim): 9
Número do jogador (0=fim): 10
Número do jogador (0=fim): 11
Número do jogador (0=fim): 10
Número do jogador (0=fim): 50
Informe um valor entre 1 e 23 ou 0 para sair!
Número do jogador (0=fim): 9
Número do jogador (0=fim): 9
Número do jogador (0=fim): 0

Resultado da votação:

Foram computados 8 votos.

Jogador Votos           %
9               4               50,0%
10              3               37,5%
11              1               12,5%
O melhor jogador foi o número 9, com 4 votos, correspondendo a 50% do total de votos.
'''




########## PROGRAMA ###########

def cabecalho():
    print ("Enquete: Quem foi o melhor jogador? \n")
    print ("Informe um valor entre 1 e 23 ou 0 para sair! \n")

Resultado = open('Resultado da Pesquisa.txt', 'w')
Resultado.write("Enquete: Quem foi o melhor jogador? \n")
Resultado.write("\n")
Resultado.write("Informe um valor entre 1 e 23 ou 0 para sair! \n")

cabecalho()

votos = []
jogador = 1
joga = []
maior = []
maior_porc = []
maior_joga = 1
maior_i = 1

while jogador != 0:
    jogador = int(input("Número do jogador (0=fim): "))
    
    if jogador < 23 and jogador != 0:
        joga.append(jogador)

    if jogador < 0 or jogador > 23:
        print("Informe um valor entre 1 e 23 ou 0 para sair!")

print('\n')

for i in range(1,24):
    votos.append(joga.count(i))
    if joga.count(i) > maior_joga:
        maior_joga = joga.count(i)
        maior_i = i

Resultado.write('\n')
Resultado.write('===================================================== \n')  
Resultado.write('================ RESULTADO DOS VOTOS ================ \n')
Resultado.write('===================================================== \n')
Resultado.write('\n')
Resultado.write("Foram computados %i votos. \n" %len(joga))
Resultado.write('\n')
Resultado.write('Jogador \t\t Votos \t\t' '  % \n')



for i in range(1,24):
   
    if joga.count(i) > 0 and joga.count(i)/sum(votos) * 100 > 0:
        (i, joga.count(i), (joga.count(i)/sum(votos) * 100))
        Resultado.write('   ')
        Resultado.write(str(i))
        Resultado.write('\t\t\t   ')
        Resultado.write(str(joga.count(i)))
        Resultado.write('\t\t')
        Resultado.write(str('{:>5.2f}'.format(joga.count(i)/sum(votos) * 100)))
        Resultado.write('\n')
    maior_porc.append(joga.count(i)/sum(votos) * 100)

maior.append(maior_i)
maior.append(max(votos))
maior.append(max(maior_porc))

Resultado.write("\n")
Resultado.write("O melhor jogador foi o número %i, com %i votos, correspondendo a %2.2f%% do total de votos."%(maior[0], maior[1], maior[2]))
      
Resultado.close()



##### PARA IMPRIMIR A PARTIR DA LINHA QUE SE DESEJA #####
Resultado = open('Resultado da Pesquisa.txt', 'r')
texto = Resultado.readlines()
for linha in range(1):
    for i in range(4, len(texto)):
        print("%s"%texto[i], end = '')
Resultado.close()


