"""
Listas em Python
Tipo list - Mutável
Suporta vàrios valores de qualquer tipo
Conhecimentos reutilizaveis - indices e fatiamento
Métodos úteis: 
append, insert, pop, del, clear, extend,+

Create Read Update   delete  ..........(CRUD)
criar , ler, alterar,apagar = lista[i] (CRUD)
"""
#Tipo list - Mutável
lista = [1,2,3,4]
#numero = lista[2] #estar jogando indice dois na variavel (numero)
lista[2] = 300 #alterar valor no indice 2
del lista[2] #apagar valor no indice 2
print(lista)
lista.append(1000) #adicionar valor ao final da lista
lista.append(2000) 
lista.append(3000)
print(lista) 
removido = lista.pop() #jogar valor na variavel e ecluir
print(lista,'Removido',removido ) #exclui ultimo valor da lista

