"""
Iteraveis -> str, range ,etc
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o proximo valor
iter -> me entregue seu iterador

"""
#numeros = range(0, 100, 8)

#for numero in numeros :
#    print(numero)

#texto = iter('sivaldo') # _iter_() = iter('sivaldo)

#print(next(texto))      # _next_() = next(texto) =entrega proximo valor


texto = 'sivaldo' #iteravel

iterador = iter(texto)

while True:
    try:
        letra = next(iterador)
        print(letra)
    except StopIteration:
        break