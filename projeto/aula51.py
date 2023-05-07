"""
Introdução ao desmpacotamento 
"""




nome1, *resto =  ['maria','vera','lucia']
print(nome1, resto)

# *_ indica que não irei usar essa variável
nome1, *_ =  ['maria','vera','lucia']
print(nome1, resto)


_, _, nome =  ['maria','vera','lucia']
print(nome)