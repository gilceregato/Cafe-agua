def calcula_prop_agua_mineral(bicarbonato, calcio, magenesio):
    alcalinidade = bicarbonato * 0.8
    dureza_Ca = calcio * 2.5
    dureza_Mg = magenesio * 4.12
    dureza_total = dureza_Ca + dureza_Mg

    return alcalinidade, dureza_Ca, dureza_Mg, dureza_total

def calcula_blend(agua_1, agua_2, alcalinidade_desejada, volume_desejado):
    alcalinidade_1 = agua_1[0]
    alcalinidade_2 = agua_2[0]
    prop_1 = (alcalinidade_desejada - alcalinidade_2)/(alcalinidade_1 - alcalinidade_2)
    prop2 = 1 - prop_1

    volume_1 = volume_desejado * prop_1
    volume_2 = volume_desejado * prop2

    ## Inserir calculo da dureza.
    dureza_Ca_blend = agua_1[1] * prop_1 + agua_2[1] * prop2
    dureza_Mg_blend = agua_1[2] * prop_1 + agua_2[2] * prop2
    dureza_total_blend = dureza_Ca_blend + dureza_Mg_blend

    return volume_1, volume_2, dureza_Ca_blend, dureza_Mg_blend, dureza_total_blend

def converte_alcalinidade_bicarbonato (alcalinidade):
    bicarbonato = alcalinidade * 1.25

    return bicarbonato

if __name__ == '__main__':
    print('teste')

    agua_1 = calcula_prop_agua_mineral(200, 39.07, 5)
    agua_2 = calcula_prop_agua_mineral(50, 8.8,2)

    volumes = calcula_blend(agua_1=agua_1, agua_2=agua_2, alcalinidade_desejada=60, volume_desejado=300)

    print(volumes)

    bicarbonato = converte_alcalinidade_bicarbonato(35)
    print(bicarbonato)