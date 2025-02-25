import streamlit as st
from Menu import calcula_mistura_agua, calcula_prop_agua_mineral
# ----------------------------------------------------------------------
if __name__ == '__main__':

    # Configurando a página inicial
    st.set_page_config(
        layout= 'wide', #formato da página,
        page_title='Diluição' #título da página
    )

    with st.sidebar:
        st.write('## Calculadora de águas para café')
        st.write('Este app foi construído utilizando como base a calculadora do Thiago Motta (@thiagomottaas)')
        st.write('para mais informações acesse:')
        st.page_link("https://www.instagram.com/thiagomottaas/", label="@thiagomottaas", icon="📷")
        st.divider()
        st.write('Criado por Gilmar Ceregato @2025')

    st.write('## Calculadora de águas para Café')
    st.write('Diluição da água mineral utilizando água destilada')

    col1, col2, col3 = st.columns([3,1,3])

    with col1:
        st.write('### Propriedade da água mineral que irá utilizar:')
        st.write('Insira abaixo as propriedades minerais do rótulo da água')
        bicarbonato = float(st.number_input("Bicarbonato (mg/L):", value=100.0, step=5.0))
        calcio = float(st.number_input("Cálcio (mg/L):", value=100.0, step=5.0))
        magnesio = float(st.number_input("Magnésio (mg/L):", value=100.0, step=5.0))

        agua_mineral = calcula_prop_agua_mineral(bicarbonato=bicarbonato, calcio=calcio, magenesio=magnesio)

        st.warning(f" A alcalinidade atual é de {agua_mineral[0]:.2f} ppm", icon="⚠️")

    with col3:
        st.write('## Propriedades desejadas para a mistura final:')
        st.write('Insira abaixo as propriedades desejadas para a mistura final')
        alcalinidade_desejada = float(st.number_input("Alcalinidade desejada (ppm):", value=30.0,step=10.0))
        if alcalinidade_desejada > agua_mineral[0]:
            st.warning("A alcalinidade desejada deve ser menor que a alcalinidade da água mineral utilizada", icon="🚨")
        volume_desejado = float(st.number_input("Volume final desejado (ml):", value=500.0, step=50.0))

    if alcalinidade_desejada >= agua_mineral[0]:
        st.warning("Impossível calcular! A alcalinidade desejada deve ser menor que a alcalinidade da água mineral utilizada", icon="🚨")
    else:
        mistura = calcula_mistura_agua(alcalinidade_desejada=alcalinidade_desejada, volume_desejado=volume_desejado, alcalinidade=agua_mineral[0], dureza_Ca=agua_mineral[1], dureza_Mg=agua_mineral[2])
        st.divider()
        st.write("## Receita da mistura:")
        st.write("### Misture as águas na seguinte proporção")
        st.write(f"1 - {mistura[4]:.2f} ml de água mineral")
        st.write(f"2 - {mistura[5]:.2f} ml de água destilada")
        st.write('')
        st.write("### A água resultante terá as seguintes propriedades:")
        st.write(f"- Alcalinidade {mistura[0]:.2f} ppm")
        st.write(f"- Dureza Ca {mistura[1]:.2f} ppm")
        st.write(f"- Dureza Mg {mistura[2]:.2f} ppm")
        st.write(f"- Dureza total {mistura[3]:.2f} ppm")
        st.write('obs.: valores em ppm de CaCO3')
