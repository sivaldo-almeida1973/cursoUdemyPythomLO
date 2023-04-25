"""
CONSTANTE = 'Variáveis' que não vão mudar
muitas condições no mesmo if (ruim)
....<- Contagem de complexidade (ruim)

"""
velocidade = int(input('Digite a velocidade do carro: '))   #velocidade atual do carro
local_carro = 101 #local (KM) em que o carro está na estrada

#CONSTANTE = 'Variáveis' que não vão mudar ,digitar em (maiusculas)

RADAR_1 = 60   # velocidade máxima do radar 1
LOCAL_1 = 100  #local onde o radar 1 está
RADAR_RANGER = 1 #a distância onde o radar começa vê o carro

if velocidade > RADAR_1:
    print(f'sua velocidade no radar 1: {velocidade} km/h')

if local_carro >= (LOCAL_1 - RADAR_RANGER) and \
    local_carro <= (LOCAL_1 + RADAR_RANGER) and \
    velocidade > RADAR_1:
    print('Carro multado em Radar_1!')

