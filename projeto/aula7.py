#variáveis são usadas para salvar algo na memória do computador
#PEP8: indica iniciar variáveis com letras minusculas, pode usar #números e underline _ .
#O sinal de = é o operador  de atribuição.Ele é usado 
#para atribuir um valor a um nome(variável).
#Uso : nome_variavel = expressão 

nome_completo = 'sivaldo vieira de almeida'
soma_dois_mais_dois = 2 + 2
print(nome_completo, soma_dois_mais_dois)


print('-'*30)
int_um = int('1')

print(int('1'), type(int('1')))#esse codigo trará o mesmo resultado 
print(int_um, type(int_um))#simplificação do codigo acima usando variável

nome = 'sivaldo'
idade = 30
maior_idade = idade >= 18
print('Nome:' ,nome , 'Idade:' ,idade)
print('É Maior de idade?', maior_idade)