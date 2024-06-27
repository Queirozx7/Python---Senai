#DESAFIO TEMPERATURA (EXTRA)

qnt_analisadas = int(input('Quantas pessoas deseja analisar: '))
fim= qnt_analisadas+1
somatoria=0
print('==============================================')
for i in range(1,fim):
    #print(i)
    temperatura = float(input('Digite a temperatuda (°C): '))
    somatoria = somatoria=temperatura
    temp_user = temperatura
    if temperatura<=37.2:
        print(f'A temperatura {temp_user} indica: NORMAL')
    elif temperatura>37.2 and temperatura<=38:
        print(f'A temperatura {temp_user}indica: FEBRIL' )
    elif temperatura>38 and temperatura<=39:
        print(f'A temperatura {temp_user} indica: FEBRE' )
    else:
        print(f'A temperatura {temp_user} indica: FEBRE ALTA ')
    print('======================================')
media = somatoria/qnt_analisadas
print(f'Media da temperatura de {qnt_analisadas} pessoas = {media} °C')