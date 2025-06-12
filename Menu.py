# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------
# Created By  : Gilmar Ceregato
# Created Date: 22/02/2025
# Changed Date: 12/07/2025
# version ='1.1'
# ----------------------------------------------------------------------
#Esse script cria um webapp em Streamlit que ajuda nos cálculos de modulação da água para o café
# ele foi criado com base nas calculadoras do Tiago Motta (thiagomottaas)
#
#	Exemplo(s):
#		Examples
#
#	Attributes:
#		Nome_atributo (type): descrição do atributo
#
#		Exemplo: module_level_variable1 (int): A variável de Module level serve
#		para identificar X...
#
#	To-dos:
#		* Task 01
#		* Task 02
# ----------------------------------------------------------------------
__author__ = 'Gilmar Ceregato' 
__copyright__ = 'Copyright 2025, Calculadora Águas para Café' 
__credits__ = ['Thiago Motta (thiagomottaas)',] 
#credits inclui as pessoas que reponrtaram bugs, fizeram sugestões, etc, mas que não escreveram o código. 
__email__ = 'gilceregato@gmail.com' 
__status__ = 'Development' # (Prototype, Development or Production)
# ----------------------------------------------------------------------
# Imports
import streamlit as st
from funcoes import converte_alcalinidade_bicarbonato

# ----------------------------------------------------------------------
# Funções 

# ----------------------------------------------------------------------
if __name__ == '__main__':
    # Configurando a página inicial
    st.set_page_config(
        layout= 'wide', #formato da página,
        page_title='Calculadora de águas para café' #título da página
    )

    with st.sidebar:
        st.write('## Calculadora de águas para café')
        st.write('Este app foi construído utilizando como base a calculadora do Thiago Motta (@thiagomottaas)')
        st.divider()
        st.write('Criado por Gilmar Ceregato @2025')

    
    st.title('Calculadora de águas para Café')

    st.write('### Utilize os menus da barra lateral para acessar os módulos específicos da calculadora')
    st.divider()

    st.write('## Conversor rápido de alcalinidade para bicarbonato')
    bicarbonato = float(st.number_input("Bicarbonato (mg/L):", value=100.0, step=5.0, key='bicarbonato_rapido'))
    alcalinidade = converte_alcalinidade_bicarbonato(bicarbonato)
    st.success(f"Alcalinidade equivalente: {alcalinidade:.2f} ppm")