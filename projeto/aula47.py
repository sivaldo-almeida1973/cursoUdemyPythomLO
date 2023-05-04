"""
Exercicio>
Faça um jogo para o usuario adivinhar a palavra secreta.
-voce vai propor uma palavra secreta qualquer e vai dar a possibildade para o usuario digitar apenas uma letra.
-quando o usuario digitar uma letra, voce vai conferir se a letra
digitada está na palavra secreta.
----se a letra digitada estiver na palavra secreta:Exiba a letra.
----se não estiver : Exiba *.
---- Faça a contagem de tentativas do seu usuário.
"""
import os


print('=====Jogo da Palavra Secreta=====')


palavra_secreta = 'sivaldo'

letras_acertadas = '' #salvar letras acertadas
numero_tentativas = 0


while True:
   
    letra_digitada = input('Digite uma letra: ')
    numero_tentativas += 1

    if len(letra_digitada) > 1:
        print('Digite apenas uma letra')
        continue #volta no começo do laço

    if letra_digitada in palavra_secreta: #salvar letras acertadas
        letras_acertadas += letra_digitada 

    palavra_formada = ''

    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
          palavra_formada += '*'
    print('Palavra_formada:', palavra_formada)

    if palavra_formada == palavra_secreta:
        os.system('cls')
        print('VOCÊ GANHOU! PARABÉNS!!')
        print('Palavra Secreta Era!!:', palavra_secreta)
        print('Tentativas:',numero_tentativas)

        letras_acertadas = '' #salvar letras acertadas
        numero_tentativas = 0
  