#Formatação de Strings

nome = 'Sivaldo Vieira DE Almeida'
altura = 1.72
peso = 86.0
imc = peso /( altura ** 2)

#print('Seu Nome é:',nome)
#print('Sua  Altura é:',altura)
#print('Peso:',peso)
#print('IMC:',imc)

print('seu NOME : {}, voce mede ALTURA: {} , sua PESO : {}KG então esse será seu IMC :{:.2f}!! \nPrecisa fazer um regime {}!!'.format(nome,altura,peso,imc,nome))

#f-strings
print(f'Seu Nome:{nome}, sua altura:{altura} ,Seu Peso:{peso},seu imc:{imc:.2f}')