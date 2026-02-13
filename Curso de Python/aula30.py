velocidade = 61
local_carro = 90

RADAR_1 = 60
LOCAL_1 = 100
RADAR_RANGE = 1

if velocidade > RADAR_1:
    print('O carro está numa velocidade maior que o radar')
    if local_carro >= (LOCAL_1 - RADAR_RANGE) and local_carro <= (LOCAL_1 - RADAR_RANGE):
        print('Foi multado')
    else:
        print('Não foi multado')
else:
    print('O carro está na velocidade permitida')

