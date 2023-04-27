"""
Repetições
While (enquanto)
Executa uma ação enquanto uma condição for verdadeira
loop infinito-> Quando um codigo não tem fim
"""

condicao = True

while condicao:
   nome = input('Qual seu nome? ')
   print(f'seu nome é {nome}')

   if nome == 'sair': 

    break #acaba com o laço

print('Acabou!!')