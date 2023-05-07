"""
Enumerate - enumera iteráveis (índices)
ira imprimir parecido com isso:
[(0,'maria'), (1,'helena'),( 2,'carla')]
"""

lista = ['maria', 'helena','carla']
lista.append('joão') #adiciona na lista no final


print(10*'==')

for item in enumerate(lista):#imprima uma tupla com indices um abaixo do outro
    a,b = item
    print(a, b)# a = indice b= valor

print(10*'==')
#mesma coisa do de cima ,essa é a melhor maneira
for indice ,nome in enumerate(lista):
    print(indice, nome)
    


print(10*'==')
for item in enumerate(lista):
    indice , nome = item
    print(indice, nome)

print(10*'==')
for tupla_enumerada in enumerate(lista):
    for valor in tupla_enumerada:
        print(valor)



print(10*'==')
for tupla_enumerada in enumerate(lista):
    print('For da tupla:')
    for valor in tupla_enumerada:
        print(f'\t{valor}')#\t dá espaços na linha