
'''Orientações:
1 - Todos os valores de alcalinidade e dureza estão em unidade de "ppm da CaCO3"
2 - A alcalinidade desejada deve ser menor que a alcalinidade da água mineral utilizada
'''
def calcula_prop_agua_mineral(bicarbonato, calcio, magenesio):
    alcalinidade = bicarbonato * 0.8
    dureza_Ca = calcio * 2.5
    dureza_Mg = magenesio * 4.12
    dureza_total = dureza_Ca + dureza_Mg

    return alcalinidade, dureza_Ca, dureza_Mg, dureza_total

def calcula_mistura_agua (alcalinidade_desejada, volume_desejado, alcalinidade, dureza_Ca, dureza_Mg):
    proporcao = alcalinidade / alcalinidade_desejada
    alcalinidade_final = alcalinidade / proporcao
    dureza_Ca_final = dureza_Ca / proporcao
    dureza_Mg_final = dureza_Mg / proporcao
    dureza_total_final = dureza_Ca_final + dureza_Mg_final

    volume_mineral = volume_desejado / proporcao
    volume_destilado = volume_desejado - volume_mineral

    return alcalinidade_final, dureza_Ca_final, dureza_Mg_final, dureza_total_final, volume_mineral, volume_destilado

def converte_alcalinidade_bicarbonato (alcalinidade):
    bicarbonato = alcalinidade * 1.25

    return bicarbonato

if __name__ == '__main__':
    print("######################################")
    print("Bem-vindo a calculadora de preparo de água!")
    print("######################################")
    print("Insira as informações da água mineral:")
    bicarbonato = float(input("Bicarbonato (mg/L):"))
    calcio = float(input("Cálcio (mg/L):"))
    magnesio = float(input("Magnésio (mg/L):"))

    agua_mineral = calcula_prop_agua_mineral(bicarbonato=bicarbonato, calcio=calcio, magenesio=magnesio)

    print("######################################")
    print(f"A alcalinidade atual é de {agua_mineral[0]:.2f} ppm")

    alcalinidade_desejada = float(input("Alcalinidade desejada (ppm):"))
    volume_desejado = float(input("Volume desejado (ml):"))

    mistura = calcula_mistura_agua(alcalinidade_desejada=alcalinidade_desejada, volume_desejado=volume_desejado, alcalinidade=agua_mineral[0], dureza_Ca=agua_mineral[1], dureza_Mg=agua_mineral[2])

    print("######################################")
    print("Resultados:")
    print("Misture as águas na seguinte proporção")
    print(f"- {mistura[4]:.2f} ml de água mineral")
    print(f"- {mistura[5]:.2f} ml de água destilada")
    print("######################################")    
    print("A água resultante terá as seguintes propriedades:")
    print(f"Alcalinidade {mistura[0]:.2f} ppm")
    print(f"Dureza Ca {mistura[1]:.2f} ppm")
    print(f"Dureza Mg {mistura[2]:.2f} ppm")
    print(f"Dureza total {mistura[3]:.2f} ppm")