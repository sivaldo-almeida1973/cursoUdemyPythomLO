"""
while/esle
"""
string = 'valorqaulquer'

i = 0 #index para contar a variavel( i )que representa o (indice)
while i < len(string):
    letra = string[i] #pegando cada uma das letras sa string
    
    if letra == ' ':
        break

    print(letra)
    i += 1

else:
    print('Não encontrei o espaço na string')

print('fora do while')