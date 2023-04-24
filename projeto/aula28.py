"""
Peça ao usuário para digitar seu nome
peça ao usuário para digitar sua idade
se o nome e a idade forem digitados:
   Exiba:
      seu nome é {nome}
       seu nome invertido é {nome invertido}

"""

nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')

if nome and idade :
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido : {nome[::-1]} ')
    if ' ' in nome:
      print(f'Seu nome {nome} contem espaços')
    else:
       print(f'Seu nome {nome} não contem espaços:')
    print(f'seu nome tem {len(nome)} letras')
    print(f'a primeira letra do seu nome: {nome[0]}')
    print(f'a ultima letra do seu nome: {nome[-1]}')
else:
    print(f'Você deixou campos vazios!')

