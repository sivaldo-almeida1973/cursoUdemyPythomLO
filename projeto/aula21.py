#operadores lógicos 
# and(e) or(ou) not(não)
#and-> ambas as condições são verdadeiras
#se qualquer valor for considerado falso,a expressão inteira 
#será tambem será.
#são considerados Falsy 0, 0.0 ,'' , False.
#tambem existe o None

entrada = input('[E]entrar  [S]sair: ')
senha_digitada = input('Senha')

# if condicao 
senha_permitida = '1010'
if entrada == 'E' and senha_digitada == senha_permitida:
    print('Entrar')
else:
    print('Sair')


print(30*'=')

print(True and True)

#avaliação de curto circuito
print(True and False and True)

#string vazia é False
print('')