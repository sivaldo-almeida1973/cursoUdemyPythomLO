"""CALCULADORA COM WHILE"""
"""
mult_num = 10
numerador = 10

num = 1
res = ''
while num <= mult_num:

    numerador_2 = 1
    while numerador_2 <= numerador:
        print(f'{num}*{numerador_2}={res}') 

        numerador_2 += 1
    res = num * numerador_2
    num += 1
print('Fim')   


"""
#sair = sair.lower() #converter maiusculo para minusculo
#sair = sair.startswith('s')# começa com (s) retorna boolean

while True:
    numero_1 = input('Digite um numero:')
    numero_2 = input('Digite outro numero:')
    operador = input('Digite o operador (+-/*):')

    numeros_validos = None
    num_1_float = 0
    num_2_float = 0
   
    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        numeros_validos = True

    except :

        numeros_validos = None

    if numeros_validos is None:
        print('Um ou ambos os numeros digitados são invalidos.')
        continue

    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos:
         print('Operador invalido.')
         continue
    
    if len(operador) > 1:
        print('digite apenas um operador!')
        continue
    
    print('Realizando sua conta.Resultado abaixo!')
    if operador == '+':
        print(f'{num_1_float} + { num_2_float} =', num_1_float + num_2_float)

    elif operador == '-':
        print(f'{num_1_float} - { num_2_float} =',num_1_float + num_2_float)


    elif operador == '*':
        print(f'{num_1_float} * { num_2_float} =',num_1_float * num_2_float)


    elif operador == '/':
        print(f'{num_1_float} / { num_2_float} =',num_1_float / num_2_float)

    else:
        print('Nunca deveria chegar aqui.')


    sair = input('Quer sair? [s]sim: ').lower().startswith('s')
    print(sair)
    

    if sair is True:
        break
