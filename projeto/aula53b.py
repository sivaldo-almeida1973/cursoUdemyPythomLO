"""
Enumerate - enumera iteráveis (índices)
ira imprimir parecido com isso:
[(0,'maria'), (1,'helena'),( 2,'carla')]
"""

lista = ['maria', 'helena','carla']
lista.append('joão') #adiciona na lista no final

lista_enumerada = list( enumerate(lista, start=20))#imprime lista enumerada
print(lista_enumerada)

for item in enumerate(lista):#imprima uma tupla com indices um abaixo do outro
    print(item)


