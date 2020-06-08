'''
Sua organização acaba de contratar um estagiário para trabalhar no Suporte de Informática, com a intenção de fazer um levantamento nas sucatas
encontradas nesta área. A primeira tarefa dele é testar todos os cerca de 200 mouses que se encontram lá, testando e anotando o estado de cada
um deles, para verificar o que se pode aproveitar deles.
Foi requisitado que você desenvolva um programa para registrar este levantamento. O programa deverá receber um número indeterminado de entradas,
cada uma contendo: um número de identificação do mouse o tipo de defeito:
necessita da esfera; necessita de limpeza; a.necessita troca do cabo ou conector; a.quebrado ou inutilizado Uma identificação igual a zero encerra
o programa. Ao final o programa deverá emitir o seguinte relatório:
Quantidade de mouses: 100

Situação                        Quantidade              Percentual
1- necessita da esfera                  40                     40%
2- necessita de limpeza                 30                     30%
3- necessita troca do cabo ou conector  15                     15%
4- quebrado ou inutilizado              15                     15%
'''

situacao = ['necessita da esfera','necessita de limpeza','necessita troca do cabo ou conector','quebrado ou inutilizado']

proximo = 'S'

defeito = []
quantidade_mouses = []
num = 0
while proximo in "Sn":

    print('-' * 80)
    print("")
    print('Digite número do defeito: ')
    print('')
    print('1 - Esfera')
    print('2 - Limpeza')
    print('3 - Cabo ou conector')
    print('4 - Quebrado ou inutilizado')
    defe = int(input("N: "))

    if defe == 1:
        defeito.append(situacao[0])
    if defe == 2:
        defeito.append(situacao[1])
    if defe == 3:
        defeito.append(situacao[2])
    if defe == 4:
        defeito.append(situacao[3])

    print('')
    quant = int(input("Quantidade de mouses: "))
    quantidade_mouses.append(quant)

    print('')
    proximo = str(input("Cadastrar próximo [S - Sim / N - Não]: ")).strip().upper()[0]

print('\n')
print('-' * 80)
print('LISTAGEM DE EQUIPAMENTOS: ')
print('-' * 25)
print("Situação \t\t\t\t", "   Quantidade \t\t", "Percentual")
for i in range(len(quantidade_mouses)):
    print('{} - {:40} {:^10} {:^30.2f}'.format(i+1, defeito[i], quantidade_mouses[i], quantidade_mouses[i] / sum(quantidade_mouses)*100))

    
    

