'''
calculando segundo digito do CPF:

CPF : 746.824.890-70
Colete a soma dos 9 primeiro digitos do CPF,mais o primeiro digito,
multiplicando cada um dos valores por uma contagem regressiva começando de 11.

ex: 746.824.890-70 (7468248907)

 11  10   9   8   7   6   5   4   3  2 
* 7   4   6   8   2   4   8   9   0  7  <--prim digito
 77  40  54   64  14  24 40   36  0  14

Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14= 363

Multiplicar o resultado anterior por 10.
363*10 = 3630

Obter o resto da divisão da conta por 11

3630 % 11 = 0

se o resultado anterior for maior que 9:
     resultado é 0
contrario disso:
     resultado é o valor da conta
     .
o segundo digito do CPF é 0
'''


print("Verificando CPF")

cpf = '74682489070'

nove_digitos = cpf[:9]#Fatiamento do 0 ao 9,o nome não inclui
contador_regressivo_1 = 10

resultado_digito_1 = 0

for digito_1 in nove_digitos: #para cada digito em nove_digitos
  resultado_digito_1 += (int(digito_1 )* contador_regressivo_1)#passar digito para inteiro e multiplicar por contador_regressivo e somar resultados
  contador_regressivo_1 -= 1

digito_1 = ((resultado_digito_1 * 10) % 11)#resultado x 10 resto da divisão por 11

digito_1 = digito_1 if digito_1 <= 9 else 0
print(digito_1)