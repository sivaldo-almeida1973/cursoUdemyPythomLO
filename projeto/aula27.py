"""
Fatiamento de strings
 012345678
 olá mundo
-987654321

Fatiamento [i:f:p] [: :]
Obs.: a função len retorna a qtd de caracteres da str
"""
# os (:) pontos indicam o fatiamento
variavel = 'ola mundo'
print(variavel[4:])# do a até o final
print(variavel[4:9]) #esse tem o mesmo resultado
print(variavel[:9])#dessa forma começa do indice 0
print(variavel[-9:-0])#usando indices negativos
print(len(variavel[3]))
print(len(variavel))#quantos caracteres tem na variavel
print(variavel[0:9:2])#pegar do 0 ao 9 de passo 3 em 3
print(variavel[::-1])#pegar do 0 ao 9 de forma invertida que é igual a
print(variavel[-1:-10:-1])
