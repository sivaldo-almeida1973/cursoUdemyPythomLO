primeiro_valor = input('Digite 1º valor: ')
segundo_valor = input('Digite 2º valor: ')

if primeiro_valor > segundo_valor:
    print(f'primeiro valor:{primeiro_valor}, \nmaior que Segundo valor:{segundo_valor}')
elif primeiro_valor == segundo_valor:
    print(f'Primeiro valor: {primeiro_valor }\nIgual ao Segundo valor: {segundo_valor}')
else:
    print(f'segundo valor {segundo_valor} maior que primeiro valor {primeiro_valor}')