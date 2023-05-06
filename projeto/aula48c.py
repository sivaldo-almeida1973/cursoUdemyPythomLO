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

# ...... 0...1..2..3..4 indice
lista = [10,20,30,40,50]


lista.append('sivaldo vieira')
nome_excluido = lista.pop()
print(lista, 'Nome', nome_excluido)
