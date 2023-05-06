"""
Listas em Python
Tipo list - Mutável
Suporta vàrios valores de qualquer tipo
Conhecimentos reutilizaveis - indices e fatiamento
Métodos úteis: 
append, insert, pop, del, clear, extend,+

...append - adicionar no final da lista
...insert - adicionar no indice escolhido da lista
...pop -    Remove no final da lista ou no indice escolhido
...del    - apaga um indice lista
...clear  - limpa a lista
...extend - estende a lista
...+      - concatena a listas

Create Read Update   delete  ..........(CRUD)
criar , ler, alterar,apagar = lista[i] (CRUD)

"""

lista_a = [1,2,3]
lista_b = [4,5,6]

lista_c = lista_a + lista_b
lista_a.extend(lista_b)
print(lista_a)