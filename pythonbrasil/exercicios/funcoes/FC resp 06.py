'''
Faça um programa que converta da notação de 24 horas para a notação
de 12 horas. Por exemplo, o programa deve converter 14:25 em 2:25 P.M.
A entrada é dada em dois inteiros. Deve haver pelo menos duas funções:
uma para fazer a conversãoe uma para a saída. Registre a informação
A.M./P.M. como um valor ‘A’ para A.M. e ‘P’ para P.M. Assim, a função
para efetuar as conversões terá um parâmetro formal para registrar se é
A.M. ou P.M. Inclua um loop que permita que o usuário repita esse cálculo
para novos valores de entrada todas as vezes que desejar.
'''

def conversorH(hora,minuto):

    print('-' * 30)
    print('    CONVERSOR DE HORÁRIO    ')
    print('-' * 30)

    if minuto == 0:
        minuto = '00'

    if hora > 12:
        nova_hora = hora - 12
        print("Hora convertida: {}:{} P.M.".format(nova_hora, minuto))
            
    if hora <= 12:
        nova_hora = hora + 12
        print("Hora convertida: {}:{} P.M.".format(nova_hora, minuto))

    print('-' * 30)
    novoCalc = str(input("Converter novamente: "))
    print('-' * 30)
   
    while novoCalc == "S" or novoCalc == "s":

        hora = int(input("Hora: "))
        minuto = int(input("Minutos: "))

        if minuto == 0:
            minuto = '00'

        if hora > 12:
            nova_hora = hora - 12
            print("Hora convertida: {}:{} P.M.".format(nova_hora, minuto))
            

        if hora <= 12:
            nova_hora = hora + 12
            print("Hora convertida: {}:{} P.M.".format(nova_hora, minuto))

        print('-' * 30)
        novoCalc = str(input("Converter novamente: "))
        print('-' * 30)





def calcHora():

    novoCalc = "S"
    print('-' * 30)
    print('    CONVERSOR DE HORÁRIO    ')
    print('-' * 30)

    while novoCalc == "S" or novoCalc == "s":

        hora = int(input("Hora: "))
        minuto = int(input("Minutos: "))

        if minuto == 0:
            minuto = '00'

        if hora > 12:
            nova_hora = hora - 12
            print("Hora convertida: {}:{} P.M.".format(nova_hora, minuto))
            

        if hora <= 12:
            nova_hora = hora + 12
            print("Hora convertida: {}:{} P.M.".format(nova_hora, minuto))

        print('-' * 30)
        novoCalc = str(input("Converter novamente: "))
        print('-' * 30)
