"""
Exercício
Exiba os índices da lista

"""

lista = ['Alice','lucas','Sivaldo']
lista.append('maria')
indices = range(len(lista))

for indice in indices:
    print(indice,lista[indice], type(lista[indice]) )