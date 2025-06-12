import streamlit as st
import pandas as pd

# ----------------------------------------------------------------------
if __name__ == '__main__':
    # Configurando a página inicial
    st.set_page_config(
        layout= 'wide', #formato da página,
        page_title='Banco de dados de águas minerais' #título da página
    )
    
    with st.sidebar:
        st.write('## Calculadora de águas para café')
        st.write('Este app foi construído utilizando como base a calculadora do Thiago Motta (@thiagomottaas)')
        st.divider()
        st.write('Criado por Gilmar Ceregato @2025')

    # Exibindo Db de águas minerais
    st.write('## Calculadora de águas para Café')
    st.write('Banco de dados de águas minerais')

    db_aguas = pd.read_excel('DB_Aguas_minerais.xlsx')
    st.dataframe(db_aguas)
