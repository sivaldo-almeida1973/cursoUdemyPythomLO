frase = 'O Python é uma linguagem de programação ' \
         'multiparadigma. '\
         'Python foi criado por Guido Van Rossum.'.lower()#minusculas

#print(frase.count('a')) #quantas vezes a latra (a) aparece na frase


i = 0

qtd_apareceu_mais_vezes = 0
letra_apareceu_mais_vezes = ''
while i < len(frase):
    letra_atual = frase[i]

    if letra_atual == ' ':
        i += 1
        continue

    qtd_vezes_letra_aparece_atual = frase.count(letra_atual)
    
    if qtd_apareceu_mais_vezes < qtd_vezes_letra_aparece_atual:
        qtd_apareceu_mais_vezes = qtd_vezes_letra_aparece_atual

        letra_apareceu_mais_vezes = letra_atual


    i += 1

print(f'a letra que apareceu mais vezes foi '
      f'"{letra_apareceu_mais_vezes}" que apareceu '
       f'{qtd_apareceu_mais_vezes}X' )