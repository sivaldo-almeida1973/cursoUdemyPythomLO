#Conversão de tipos, coerção
#type convertion, typecasting, coercion
#é o ato de converter um tipo em outro.

#Tipos imutáveis e primitivos:
# str , int, float, bool

print(1 + 1) # dois números inteiros geram um operação matemática

print('a' + 'b')# duas strings concatena

#print('1' + 1)# string com numero inteiro gera um erro!

#Funções para converter 

print('1')# string
print(type('1'))#verifica a class de elemento

#converter string para int
print(int('1'))# convertendo para tipo inteiro
print(type(int('1')))#verifica a class de elemento
print(int('1') + 1)#coerção para int

print('-'*10)
#converter string para float

print(float('1'))#coverte para tipo float 
print(type(float('1')))#verifica a class de elemento

print(bool(''))#string vazia gera False
print(bool(' '))# string vazia com espaço gera True

print(str(11) + 'b')#converter inteiro para str


print(type(int('1')) , type(int('1')))