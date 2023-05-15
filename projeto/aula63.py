'''
calculando primeiro digito do CPF:

CPF : 746.824.890-70
Colete a soma dos 9 primeiro digitos do CPF,multiplicando cada um dos valores por uma contagem regressiva começando de 10.

ex: 746.824.890-70 (7468248907)

  10  9   8   7   6   5   4   3   2  
* 7   4   6   8   2   4   8   9   0    <--prim digito
 70  36  48   56  30  20 32   27  0  

Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14= 363

Multiplicar o resultado anterior por 10.
301*10 = 3010

Obter o resto da divisão da conta anterior por 10

3010 % 11 = 07

se o resultado anterior for maior que 9:
     resultado é 0
contrario disso:
     resultado é o valor da conta
     .
o segundo digito do CPF é 0
'''


print("Verificando CPF")

cpf_enviado_usuario = '74682489070'

nove_digitos = cpf_enviado_usuario[:9]#Fatiamento do 0 ao 9,o nome não inclui
contador_regressivo_1 = 10

resultado_digito_1 = 0

for digito in nove_digitos: #para cada digito em nove_digitos
  resultado_digito_1 += (int(digito )* contador_regressivo_1)#passar digito para inteiro e multiplicar por contador_regressivo e somar resultados
  contador_regressivo_1 -= 1

digito_1 = ((resultado_digito_1 * 10) % 11)#resultado x 10 resto da divisão por 11
digito_1 = digito_1 if digito_1 <= 9 else 0


#Calculo do segundo digito
dez_digitos = nove_digitos + str(digito_1)
contador_regressivo_2 = 11


resultado_digito_2 = 0

for digito in dez_digitos:
  resultado_digito_2 += (int(digito)*contador_regressivo_2)
  contador_regressivo_2 -= 1

digito_2 = (resultado_digito_2 * 10 % 11) 
digito_2 = digito_2 if digito_2 <= 9 else 0



cpf_gerado_pelo_calculo = (f'{nove_digitos}{digito_1}{digito_2}')
print(cpf_gerado_pelo_calculo)

if cpf_enviado_usuario == cpf_gerado_pelo_calculo:
  print(f'{cpf_enviado_usuario} é válido')
else:
  print('CPF inválido!')
