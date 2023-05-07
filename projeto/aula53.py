"""
Enumerate - enumera iteráveis (índices)
"""

lista = ['maria', 'helena','carla']
lista.append('joão') #adiciona na lista no final

#lista_enumerada = enumerate(lista)# assim só aceita um for
#print(lista_enumerada)
#print(next(lista_enumerada))


for item in enumerate(lista):#dessa forma aceita vários for
    print(item)

for item in enumerate(lista):
    print(item)
