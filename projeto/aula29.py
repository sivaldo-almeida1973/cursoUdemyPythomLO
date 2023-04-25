"""
Introdução ao try/except
try -> (tentar executar o código)
except -> ocorreu algum erro ao tentar executar

"""
#vai iprimir string
numero_str = input('Vou dobrar o número que voce digitar: ')

try:#tente executar esse codigo digitando um numero
    num_float = float(numero_str)#converte em float
    print('float:', numero_str) #imprimir float
    print(f'o dobro de {numero_str} é {num_float * 2}')
except:#se digitar alguma coisa diferente de float cai aqui
    print('Isso não é um numero!')


#o if checa uma condição porem não evita exceções

    
