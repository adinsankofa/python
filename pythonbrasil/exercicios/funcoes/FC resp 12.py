'''
Embaralha palavra. Construa uma função que receba uma string como parâmetro e
devolva outra string com os carateres embaralhados. Por exemplo: se função
receber a palavra python, pode retornar npthyo, ophtyn ou qualquer outra
combinação possível, de forma aleatória. Padronize em sua função que todos
os caracteres serão devolvidos em caixa alta ou caixa baixa, independentemente
de como foram digitados.
'''

def embaralha():
    palavra = str(input('Digite uma palavra: '))
    import random
    embaralha = random.sample(palavra,len(palavra))
    palavra = ''.join(embaralha)
    print('MAÍUSCULA: ',palavra.upper())
    print('MINÚSCULA: ',palavra.lower())
    
    
    
