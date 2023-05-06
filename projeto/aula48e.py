"""
Cuidados com dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)

"""
#dessa forma se alterar a lista_a , tambem mudará na lista_b
lista_a = ['sivaldo','almeida']
lista_b = lista_a


lista_a[0] = 'Alice'
print(lista_b)



#nesse caso a mudança não atera a lista b
print(10*'=')

lista_a = ['sivaldo','almeida']
lista_b = lista_a.copy() #faz uma copia da lista_a para a lista_b


lista_a[0] = 'Alice'
print(lista_b)

