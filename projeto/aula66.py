"""
Argumentos nomeados e não nomeados em funçoes Python
argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)

"""

def soma(x, y):         # x , y são parametros
    print(x + y)

soma(13, 14)





def soma(x, y):         # x , y são parametros
    print(f'{x=} {y=}', '|', 'x+y =', x + y)

soma(13, 14)  
soma(y=13, x=14) #argumentos, se nomear um argumeto, terá que nomear todos depois dele



