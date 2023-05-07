"""
Faça uma lsita de compras com listas
O usuário de ter a possibilidade de:
Inserir, apagar, e listar valores  da sua lista
Não permita que o programa quebre com erros de 
indices inexistentes na lista

"""
import os

lista = []

while True:
    print('selecione uma Opção:' )
    opcao = input( '[i]inserir [a]apagar [l]listar:' )

    if opcao == 'i':
     
      valor = input('Valor: ')
      lista.append(valor)


    elif opcao == 'a':
      print('a')

    elif opcao == 'l':
       print('l')
     
    if len(lista) == 0:
       print('Nada para listar!')
    
    for i, valor in enumerate(lista):
       print(i, valor)


    else:
       print('Por favor , escolha i, a, l.')

