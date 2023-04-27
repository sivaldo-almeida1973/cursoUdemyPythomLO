"""
repetições
while (enquanto)
Executa uma ação enquanto uma codição for verdade
loop infinito-> Quando um código não tem fim
"""

qdt_linhas = 5 #condição
qtd_colunas = 5

linha = 1

while linha <= qdt_linhas:#pra cada volta da linha (5 colunas)
    coluna = 1
    while coluna <= qtd_colunas:
        print(f'{linha=}{ coluna=}')

        coluna += 1

    linha += 1

print('acabou')