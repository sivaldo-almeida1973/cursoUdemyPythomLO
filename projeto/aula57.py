"""
Lista ddentro de listas e seus indices
"""

salas = [
     #0            1
    ['Maria', 'Helena'],# 0
       #0         1
    ['elaine', 'Alice'], #1

    # 0          1          2
    ['Lucas', 'sivaldo', 'guti',(0,10,20,30,40,50)]# 2
]

print(salas)
print(salas[1]) #imprime a lista 1
print(salas[1][1]) #iprimir da lista 1 indice 1
print(salas[2][1]) #iprimir da lista 2 indice 1
print(salas[0][1]) #iprimir da lista 0 indice 1
print(salas[2][3][4]) #iprimir da lista 2 indice 3 o indice 4

print(20*'=')

for sala in salas:
    print(f'A sala é : {sala}')
    for aluno in sala:
     print(aluno)