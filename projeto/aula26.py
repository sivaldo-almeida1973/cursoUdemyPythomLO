#FORMATAÇÃO BÁSICA DE STRINGS
# S - String
# d - int
# f - float
# .< número de dígitos> f
# x ou X -Hexadecimal
# (carctere) (>< ^)(quantidade)
# > - irá criar espaços na esquerda
# < - irá criar espaços na direita
# ^ - centralizar 
variavel = 'MENU'
print(f'{variavel}')
print(f'{variavel:>10}')
print(f'{variavel:<10}')
print(f'{variavel:^10}')
print(f'{variavel:$^10}')
print(f'{variavel:=^10}')
# sinal - + ou -
# ex: 0 > - 100, .1f colocar virgula tambem
print(f'{-1000.3475869044:,.2f}')
print(f'{+1000.3475869044:+,.2f}')#mostrar negativo ou positivo tambem
print(f'o hexadecimal de 1500 é {1500:08x}')

# conversion flags - !r !s !a
























