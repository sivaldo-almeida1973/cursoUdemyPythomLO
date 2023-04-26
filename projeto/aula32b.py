hora = input('Digite a hora atual:')

try:
   hora_int = int(hora)
   if hora_int >= 0 and hora_int <= 11:
     print('Bom dia!')
   elif hora_int >= 12 and hora_int <= 17:
     print('Boa tarde!')

   elif hora_int >= 18 and hora_int <= 23:
     print('Boa noite!')
   else:
     print('Hora inválida!')

  
except:
    print('Por favor digite um numero inteiro')