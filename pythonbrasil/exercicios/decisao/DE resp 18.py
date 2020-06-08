'''
Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a
mesma é uma data válida.
'''


### ALGORITMO (até ano válido 2017)

def main():

    def data():

        global a
   
        Data = []
        dia = int(input('Dia (dd): '))
        Data.append(dia)
        mês = int(input('Mês (mm): '))
        Data.append(mês)
        ano = int(input('Ano (aaaa): '))
        Data.append(ano)
        if 1 <= Data[0] <= 31 and 1 <= Data[1] <= 12 and 1 <= Data[2] <= 2017:
            print('')
            a = ('O dia %2i/%2i/%4i é uma data válida.'%(Data[0], Data[1], Data[2]))
            if Data[0] < 10:
                a = ('O dia 0%s/%i/%4i é uma data válida.'%(Data[0], Data[1], Data[2]))
            if Data[1] < 10:
                a = ('O dia %i/0%s/%4i é uma data válida.'%(Data[0], Data[1], Data[2]))
            if Data[0] < 10 and Data[1] < 10:
                a = ('O dia 0%s/0%s/%4i é uma data válida.'%(Data[0], Data[1], Data[2]))
            print (a)
            print('')
        else:
            a = 0

    def datase0():
        while a == 0:
            print('')
            print("Data inválida, tente novamente... ")
            print('')
            data()

    data()
    if a == 0:
        datase0()

main()





### FUNÇÃO ###

def data_valida(dia, mês, ano):
    Data = []
    Data.append(int(dia))
    Data.append(mês)
    Data.append(ano)
    if 1 <= Data[0] <= 31 and 1 <= Data[1] <= 12 and 1 <= Data[2] <= 2017:
        a = ('O dia %2i/%2i/%4i é uma data válida.'%(Data[0], Data[1], Data[2]))
        if Data[1] < 10:
            a = ('O dia %2i/0%s/%4i é uma data válida.'%(Data[0], Data[1], Data[2]))
        print (a)
    else:
        print("Data inválida, tente novamente... ")

