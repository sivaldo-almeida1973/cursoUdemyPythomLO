#Desempacotamento eem chamadas
#de metodos e funções

string = 'ABCD'
lista = ['Maria','Alice',1,2,3,'Joana']
tupla = ('Python', 'é', 'legal')

#a,b, *_,ap,u = lista
#print(a,u,ap)

#for nome in lista:#irá imprimir cada item lista  um abaixo do outr
 #   print(nome)


#for nome in lista:
#   print(nome, end=' ,')#imprimir itens da lista separado por vigulas


print(*lista)
print(*string)
print(*tupla)


print(20*'==')
salas = [
     #0            1
    ['Maria', 'Helena'],# 0
       #0         1
    ['elaine', 'Alice'], #1

    # 0          1          2
    ['Lucas', 'sivaldo', 'guti',(0,10,20,30,40,50)]# 2
]


print(*salas)
print(*salas, sep=' \n')#separa lista por lista
