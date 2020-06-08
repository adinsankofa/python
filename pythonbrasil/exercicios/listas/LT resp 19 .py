'''
Uma empresa de pesquisas precisa tabular os resultados da seguinte enquete feita a um grande quantidade de organizações:
"Qual o melhor Sistema Operacional para uso em servidores?"

As possíveis respostas são:

1- Windows Server
2- Unix
3- Linux
4- Netware
5- Mac OS
6- Outro

Você foi contratado para desenvolver um programa que leia o resultado da enquete e informe ao final o resultado da mesma. O programa
deverá ler os valores até ser informado o valor 0, que encerra a entrada dos dados. Não deverão ser aceitos valores além dos válidos
para o programa (0 a 6). Os valores referentes a cada uma das opções devem ser armazenados num vetor. Após os dados terem sido completamente
informados, o programa deverá calcular a percentual de cada um dos concorrentes e informar o vencedor da enquete. O formato da saída foi dado
pela empresa, e é o seguinte:
Sistema Operacional     Votos   %
-------------------     -----   ---
Windows Server           1500   17%
Unix                     3500   40%
Linux                    3000   34%
Netware                   500    5%
Mac OS                    150    2%
Outro                     150    2%
-------------------     -----
Total                    8800

O Sistema Operacional mais votado foi o Unix, com 3500 votos, correspondendo a 40% dos votos.
'''

### FUNÇÃO DE IMPRESSÃO ###

def lte(x,y,z):
    
    limite = 0
    limite2 = 0
    limite3 = 0
    
    espaço = []
    espaço2 = []
    espaço3 = []
    
    for i in range(len(x)):
        if len(x[i]) > limite:
            limite = len(x[i])
        if len(str(y[i])) > limite2:
            limite2 = len(str(y[i]))
        if len(str(z[i])) > limite3:
            limite3 = len(str(z[i]))

    for i in range(len(x)):
        dif = limite - len(x[i])
        espaço.append(dif * ' ')
        dif2 = limite2 - len(str(y[i]))
        espaço2.append(dif2 * ' ')
        dif3 = limite3 - len(str(z[i]))
        espaço3.append(dif3 * ' ')
        

    for i in range(len(x)):
        print('%i - %s'%(i+1,x[i]), espaço[i] + 6 * ' ', espaço2[i], y[i], espaço3[i] + 7 * ' ', z[i])




### ALGORITMO ###

print("Qual o melhor Sistema Operacional para uso em servidores? \n")
print("Escolha uma das opções abaixo relacionadas: \n")

SO = [0,'Windows Server', 'Unix', 'Linux', 'Netware', 'Mac OS', 'Outro']
votos =[]
for i in range(1,len(SO)):
    print('%i - %s'%(i, SO[i]))
    
print('\n')

resposta = 1
while resposta != 0:
    resposta = int(input("Resposta: "))
    if resposta <= 6 and resposta != 0:
        votos.append(resposta)
    if resposta < 0 or resposta > 6:
        print("Número de resposta inválido, digite novamente \n")

print('\n')
        
formato_geral = []
formato1 = []
formato2 = []
formato3 = []
votos_porcento = []
maior_i = 1
maior = 0
SO_maisvotado = []

for i in range(len(SO)):

    votos_porcento.append(votos.count(i) / len(votos) * 100)

    if SO[i] != 0:
        formato_geral.append([SO[i], votos.count(i), '%1.f%%'%votos_porcento[i]])
        formato1.append(SO[i])
        formato2.append(votos.count(i))
        formato3.append('%1.f%%'%votos_porcento[i])

    if votos.count(i) > maior_i:
        maior_i = votos.count(i)
        maior = i


for i in range(1):
    for j in range(len(SO)):
        c = maior
        if c == j:
            d = SO[j]
            SO_maisvotado.append([c, SO[j]])


print("Sistema Operacional: \t Votos", 4 * ' ', '  %')
print("-" * 20, '\t', "-" * 5, 5 * ' ', "-" * 3)

lte(formato1, formato2, formato3)

print("-" * 20, '\t', "-" * 5, 5 * ' ')
print("Total", ' ' * 20, sum(formato2))

            
print('\n')
print('O Sistema Operacional mais votado foi o', SO_maisvotado[0][1], 'com votos %i votos, correspondendo a %0.2f%% dos votos.'%(maior_i, max(votos_porcento)))







