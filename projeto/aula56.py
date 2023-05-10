"""
split e join com list e str
split - divide uma string

join - une uma string

"""
# sem especificar nada,  divide nos espaços vazios entre palavras
frase = '   olha só que ,coisa interessante'
lista_palavras = frase.split()#divide string por virgula e aspas nos espaços vazios
print(lista_palavras)

print(20*'==')
#especifiquei que irá cortar na virgula, usando aspas e espaço

frase = '   olha só que ,coisa interessante'
lista_frases = frase.split(', ')#divide a string na virgula
print(lista_frases)



print(20*'==')

frase = '   olha só que ,coisa interessante'
lista_frases = frase.split(',')#divide string por virgula a aspas sos espaços vazios


for i, frase in enumerate(lista_frases):
 print(lista_frases[i].strip())#strip() corta espaços



print(20*'==')

frase = '   olha só que ,coisa interessante'
lista_frases = frase.split(',')#divide string por virgula a aspas sos espaços vazios


for i, frase in enumerate(lista_frases):
 print(lista_frases[i].strip())#strip() corta espaços

