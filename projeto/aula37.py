"""
Repetições
While (enquanto)
Executa uma ação enquanto uma condição for verdadeira
loop infinito-> Quando um codigo não tem fim

"""

#break 
#contador = 0

#while contador <= 10:
 #   contador += 1
 #   print(contador)

#    if contador == 4:
 #       break #quebra o laço

#print('contador acabou!!')



#continue


print(20*'=')
contador = 0

while contador <= 100:
    contador += 1 #esta linha controla o while
    
    if contador == 6:
        print('Não vou mostrar o 6')
        continue #faz pular o local escolhido

    if contador >= 10 and contador <= 30:
        print('não vai mostrar ', contador)
        continue

    print(contador)

    if contador == 50:
        break #quebra o laço
 

print('contador acabou!!')