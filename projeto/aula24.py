#Operadores in (esta entre) e not in (não esta entre)
#Strings são iteráveis
# 0 1 2 3 4 5 6 indices positivos
# s i v a l d o
#-7-6-5-4-3-2-1 indices negativos

nome = 'sivaldo'
print(nome[2]) #acessar indice 2
print(nome[-5]) #acessar indice -5

print('a' in nome)# se a letra (a)esta dentro do nome
print('valdo' in nome)# se a letra (valdo)esta dentro do nome
print('x' in nome)# se a letra (x)esta dentro do nome

print(10*'=')
print('a' not in nome)# se a letra (a)não esta dentro de nome
print('valdo' not in nome)# se a letra (valdo)não esta dentro de nome

print(10*'=')
nome = input('Digite seu nome! ')
encontrar = input('Digite o que deseja encontrar: ')


if encontrar in nome:
    print(f'{encontrar} está em Nome: {nome}')
else:
    print(f'{encontrar} não está em Nome: {nome}')