print(20*'==')
#alterar indice
frase = '   olha só que ,coisa interessante'
lista_frases_cruas = frase.split(',')#divide string por virgula a aspas sos espaços vazios

lista_frases = []

for i, frase in enumerate(lista_frases_cruas):
   lista_frases.append(lista_frases_cruas[i].strip())

 
print(lista_frases_cruas)
print(lista_frases)


frases_unidas = '='.join( lista_frases)
print(frases_unidas)