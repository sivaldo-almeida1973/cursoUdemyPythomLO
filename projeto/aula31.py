"""
Flag (Bandeire) - Marcar um local
None = Não valor
is e is not = é ou não é (tipo , valor, identidade)
id = Identidade
"""
v1 = 'a'
v2 = 'a'

print(id(v1))
print(id(v2))



print(20*'=')


condicao = True
passou_no_if = None

if condicao :
   passou_no_if = True
   print('faça algo')
else:
   print('não faça algo')


if passou_no_if is None:
   print('nao passou no if')
else:
   print('pasou no if')