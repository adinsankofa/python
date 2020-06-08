'''
Faça um programa que receba a temperatura média de cada mês do ano e
armazene-as em uma lista. Após isto, calcule a média anual das
temperaturas e mostre todas as temperaturas acima da média anual,
e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro,
2 – Fevereiro, . . . ).
'''

mes = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
temp = []
temperatura = []
media = 0

for i in range(len(mes)):
    temp = float(input("Digite a temperatura de %s: " %(mes[i])))
    temperatura.append(temp)

media = sum(temperatura)/len(mes)

print("")

print("   MÊS"   "\t\t", "    TEMPERATURA")
for i in range(len(mes)):
    print(mes[i],"     \t      \t %0.2f"%temperatura[i])

print("")

print("MÉDIA ANUAL: %2.2f" %media)

print("")

print("TEMPERATURAS MAIS ALTAS: ")
for j, n in enumerate(temperatura):
    if(temperatura[j] >= media):
        print(mes[j], "= %0.2f"%temperatura[j])
