"""
Introdução ao try/except
try -> (tentar executar o código)
except -> ocorreu algum erro ao tentar executar

"""

numero_str = input('vou dobrar o número que voce digitar: ')

try:
    num_float = float(numero_str)
    print('float:', numero_str)
    print(f'o dobro de {numero_str} é {num_float * 2}')
except:
    print('Isso não é um numero!')


#o if checa uma condição porem não evita exceções

    
