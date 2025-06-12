import streamlit as st
from funcoes import calcula_prop_agua_mineral, calcula_blend

# ----------------------------------------------------------------------
if __name__ == '__main__':

    # Configurando a página inicial
    st.set_page_config(
        layout= 'wide', #formato da página,
        page_title='Blend de águas minerais' #título da página
    )
    
    with st.sidebar:
        st.write('## Calculadora de águas para café')
        st.write('Este app foi construído utilizando como base a calculadora do Thiago Motta (@thiagomottaas)')
        st.divider()
        st.write('Criado por Gilmar Ceregato @2025')

    st.write('## Calculadora de águas para Café')
    st.write('Mistura de duas águas minerais')

    col1, col2, col3 = st.columns([3,1,3])

    with col1:
        st.write('### Água mineral 01:')
        st.write('Insira abaixo as propriedades minerais da primeira água que irá utilizar')
        bicarbonato = float(st.number_input("Bicarbonato (mg/L):", value=100.0, step=5.0, key='bicarbonato 01'))
        calcio = float(st.number_input("Cálcio (mg/L):", value=100.0, step=5.0, key= 'calcio 01'))
        magnesio = float(st.number_input("Magnésio (mg/L):", value=100.0, step=5.0, key = 'magnesio 01'))

        agua_mineral_1 = calcula_prop_agua_mineral(bicarbonato=bicarbonato, calcio=calcio, magenesio=magnesio)

        st.warning(f" A alcalinidade atual da água 01 é de {agua_mineral_1[0]:.2f} ppm", icon="⚠️")

    with col3:
        st.write('### Água mineral 02:')
        st.write('Insira abaixo as propriedades minerais da segunda água que irá utilizar')
        bicarbonato_2 = float(st.number_input("Bicarbonato (mg/L):", value=100.0, step=5.0, key='bicarbonato 02'))
        calcio_2 = float(st.number_input("Cálcio (mg/L):", value=100.0, step=5.0, key= 'calcio 02'))
        magnesio_2 = float(st.number_input("Magnésio (mg/L):", value=100.0, step=5.0,key = 'magnesio 02'))

        agua_mineral_2 = calcula_prop_agua_mineral(bicarbonato=bicarbonato_2, calcio=calcio_2, magenesio=magnesio_2)

        st.warning(f" A alcalinidade atual da água 02 é de {agua_mineral_2[0]:.2f} ppm", icon="⚠️")

    st.divider()
    st.write('## Propriedades desejadas para a mistura final:')
    st.write('Insira abaixo as propriedades desejadas para a mistura final')
    alcalinidade_desejada = float(st.number_input("Alcalinidade desejada (ppm):", value=30.0,step=10.0))
    
    alcalinidade_max = max(agua_mineral_1[0], agua_mineral_2[0])
    alcalinidade_min = min (agua_mineral_1[0], agua_mineral_2[0] )
    
    if alcalinidade_desejada > alcalinidade_max or alcalinidade_desejada < alcalinidade_min:
        st.warning("A alcalinidade desejada deve ter um valor intermediário entre a alcalinidade das águas minerais utilizadas", icon="🚨")
    
    volume_desejado = float(st.number_input("Volume final desejado (ml):", value=500.0, step=50.0))

    st.divider()
    if alcalinidade_desejada > alcalinidade_max or alcalinidade_desejada < alcalinidade_min:
        st.warning("Impossível calcular! A alcalinidade desejada deve ter um valor intermediário entre a alcalinidade das águas minerais utilizadas", icon="🚨")
    else:
        if agua_mineral_1[0] >= agua_mineral_2[0]:
            agua_1 = agua_mineral_1
            agua_2 = agua_mineral_2
            volumes = calcula_blend(agua_1=agua_1, agua_2=agua_2, alcalinidade_desejada=alcalinidade_desejada, volume_desejado=volume_desejado)
            
            st.write("## Receita da mistura:")
            st.write("### Misture as águas na seguinte proporção")
            st.write(f"1 - {volumes[0]:.2f} ml da Água mineral 01")
            st.write(f"2 - {volumes[1]:.2f} ml da Água mineral 02")
            st.write('')
            st.write("### A água resultante terá as seguintes propriedades:")
            st.write(f"- Alcalinidade {alcalinidade_desejada:.2f} ppm")
            st.write(f"- Dureza Ca {volumes[2]:.2f} ppm")
            st.write(f"- Dureza Mg {volumes[3]:.2f} ppm")
            st.write(f"- Dureza total {volumes[4]:.2f} ppm")
            st.write('obs.: valores em ppm de CaCO3')
        

        if agua_mineral_2[0] > agua_mineral_1[0]:
            agua_1 = agua_mineral_2
            agua_2 = agua_mineral_1
            volumes = calcula_blend(agua_1=agua_1, agua_2=agua_2, alcalinidade_desejada=alcalinidade_desejada, volume_desejado=volume_desejado)

            st.write("## Receita da mistura:")
            st.write("### Misture as águas na seguinte proporção")
            st.write(f"1 - {volumes[1]:.2f} ml da Água mineral 01")
            st.write(f"2 - {volumes[0]:.2f} ml da Água mineral 02")
            st.write('')
            st.write("### A água resultante terá as seguintes propriedades:")
            st.write(f"- Alcalinidade {alcalinidade_desejada:.2f} ppm")
            st.write(f"- Dureza Ca {volumes[2]:.2f} ppm")
            st.write(f"- Dureza Mg {volumes[3]:.2f} ppm")
            st.write(f"- Dureza total {volumes[4]:.2f} ppm")
            st.write('obs.: valores em ppm de CaCO3')