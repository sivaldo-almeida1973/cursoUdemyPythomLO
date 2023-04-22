#Format

a = 'A'
b = 'B'
c = 1.1

formato = 'a={}, b={},c={}'.format(a,b,c)
print(formato)


a = 'A'
b = 'B'
c = 1.1


print('A={},B= {},C={}'.format(a,b,c))

#utilizando por indices posso repetir quantas vezes quiser
print('A={0},A={0},A={0},A={0},B= {1},C={2}'.format(a,b,c))


#parâmetro nomeado ,é quando dou nome as coisas, se monear o #primeiro terá que nomear o restante
print('A={},B= {},C={nome3}'.format(a, b, nome3= c))


print('A={nome1},B= {nome2},C={nome3}'.format(nome1=a, nome2=b, nome3=c))