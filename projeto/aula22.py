#Operadores lógicos
#or qualquer condição verdadeira avalia toda a expressão verdadeira
#se qualquer valor for considerado verdadeiro, a expressão inteira
#será verdadeira.
#São considerados Falsy (que você já viu) 0,0.0 ,'',False
#tambem existee o tipo None que é usado para representar um não #valor

entrada = input('[E]entrar  [S]sair: ')
senha_digitada = input('Senha')

# if condicao 
senha_permitida = '1010'
#colocar entre parenteses evitar ambiguidade 
if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
    print('Entrar')
else:
    print('Sair')


