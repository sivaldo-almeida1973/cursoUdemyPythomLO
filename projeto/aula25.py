"""
Interpolação básica de strings(mesmo resultado de format e f_strings)
s  - string
d  e i - int
f  - float
x  e X - Hexadecimal(abcdef0123456789)

"""

nome = 'sivaldo'
preco = 1000.95897643
variavel = (f'%s, o preço é R$%.2f' %(nome,preco))
print(variavel)


print('O hexadecimal de %d é %04x' % (15, 15))#minusculo
print('O hexadecimal de %d é %04X' % (15, 15))#maiusculo