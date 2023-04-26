num = input('Digite um numero inteiro: ')
num_int = int(num)

if num_int % 2 == 0 :
    print(f'O numero digitado :{num_int} é par')
else:
    print(f'o numero digitado {num_int} é impar')




print(20*'=')
entrada = input('Digite um numero inteiro: ')

if entrada.isdigit():
    entrada_int = int(entrada)
    par_impar = entrada_int % 2 == 0
    par_impar_texto = 'impar'

    if par_impar:
        par_impar_texto = 'par'
        print(f'o numero {entrada_int} é {par_impar_texto}')
else:
    print('voce não digitou um numero inteiro!')
   

   
#outra forma com o mesmo resultado
print(20*'=')
entrada = input('Digite um numero inteiro: ')

try:
    entrada_int = int(entrada)
    par_impar = entrada_int % 2 == 0
    par_impar_texto = 'impar'

    if par_impar:
        par_impar_texto = 'par'
        print(f'o numero {entrada_int} é {par_impar_texto}')
except:
    print('voce não digitou um numero inteiro!')
