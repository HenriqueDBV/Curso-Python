velocidade = 61
local_carro = 90

# VARIAVEIS EM LETRAS MAIUCUSLA SÃO CONSTANTE, OS VALORES NAO SERÃO MUDADOS 
RADAR_1 = 60
LOCAL_1 = 100
RADAR_RANGE = 1 



if velocidade > RADAR_1:
    print('Carro passou do radar 1')

if LOCAL_1 >= (LOCAL_1 - RADAR_RANGE) and \
    local_carro <= (LOCAL_1 + RADAR_RANGE) and \
        velocidade > RADAR_1:
    print('Carro Multado em radar 1')