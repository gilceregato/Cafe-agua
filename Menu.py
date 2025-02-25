# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------
# Created By  : Gilmar Ceregato
# Created Date: 22/02/2025
# version ='1.0'
# ----------------------------------------------------------------------
#Esse script cria um webapp em Streamlit que ajuda nos cálculos de modulação da água para o café
# ele foi criado com base nas calculadoras do Tiago Motta (thiagomottaas)
#
#	Exemplo(s):
#		Examples can be given using either the ``Example`` or ``Examples``
#		sections. Sections support any reStructuredText formatting, including
#		literal blocks:
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
# 

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

# ----------------------------------------------------------------------
# Funções 

def saudacao(nome): 

    #Faz uma saudação ao usuário com o nome dado. 
    #Breve descrição do que a função realiza. 

    #Parameters:

    #nome (str): O nome do usuário. 
    #parâmetro (tipo): descrição do parâmetro 

    #Returns:

    #str: Mensagem de saudação. 
    #tipo: descrição do resultado 

    return f'Olá, {nome}!' 

def calcula_prop_agua_mineral(bicarbonato, calcio, magenesio):

    #Faz uma saudação ao usuário com o nome dado. 
    #Breve descrição do que a função realiza. 

    #Parameters:

    #nome (str): O nome do usuário. 
    #parâmetro (tipo): descrição do parâmetro 

    #Returns:

    #str: Mensagem de saudação. 
    #tipo: descrição do resultado 

    alcalinidade = bicarbonato * 0.8
    dureza_Ca = calcio * 2.5
    dureza_Mg = magenesio * 4.12
    dureza_total = dureza_Ca + dureza_Mg

    return alcalinidade, dureza_Ca, dureza_Mg, dureza_total

def calcula_blend(agua_1, agua_2, alcalinidade_desejada, volume_desejado):

    #Faz uma saudação ao usuário com o nome dado. 
    #Breve descrição do que a função realiza. 

    #Parameters:

    #nome (str): O nome do usuário. 
    #parâmetro (tipo): descrição do parâmetro 

    #Returns:

    #str: Mensagem de saudação. 
    #tipo: descrição do resultado 

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

def converte_alcalinidade_bicarbonato (bicarbonato):

    #Faz uma saudação ao usuário com o nome dado. 
    #Breve descrição do que a função realiza. 

    #Parameters:

    #nome (str): O nome do usuário. 
    #parâmetro (tipo): descrição do parâmetro 

    #Returns:

    #str: Mensagem de saudação. 
    #tipo: descrição do resultado 
    alcalinidade = bicarbonato * 0.8

    return alcalinidade

def calcula_mistura_agua (alcalinidade_desejada, volume_desejado, alcalinidade, dureza_Ca, dureza_Mg):
    #Faz uma saudação ao usuário com o nome dado. 
    #Breve descrição do que a função realiza. 

    #Parameters:

    #nome (str): O nome do usuário. 
    #parâmetro (tipo): descrição do parâmetro 

    #Returns:

    #str: Mensagem de saudação. 
    #tipo: descrição do resultado 

    proporcao = alcalinidade / alcalinidade_desejada
    alcalinidade_final = alcalinidade / proporcao
    dureza_Ca_final = dureza_Ca / proporcao
    dureza_Mg_final = dureza_Mg / proporcao
    dureza_total_final = dureza_Ca_final + dureza_Mg_final

    volume_mineral = volume_desejado / proporcao
    volume_destilado = volume_desejado - volume_mineral

    return alcalinidade_final, dureza_Ca_final, dureza_Mg_final, dureza_total_final, volume_mineral, volume_destilado

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
        st.write('para mais informações acesse:')
        st.page_link("https://www.instagram.com/thiagomottaas/", label="@thiagomottaas", icon="📷")
        st.divider()
        st.write('Criado por Gilmar Ceregato @2025')

    
    st.title('Calculadora de águas para Café')
    st.info('Este app foi construído utilizando como base a calculadora do Thiago Motta (@thiagomottaas)', icon="ℹ️")


    st.write('Para mais informações sobre cursos acesse:')
    st.page_link("https://www.instagram.com/thiagomottaas/", label="@thiagomottaas", icon="📷")

    st.write('### Utilize os menus da barra lateral para acessar os módulos específicos da calculadora')
    st.write('### Ou se preferir utilize os links abaixo:')

    st.page_link("pages/01_Diluição.py", label="Diluição em água destilada", icon="1️⃣")
    st.page_link("pages/02_Blend de águas minerais.py", label="Blend de águas minerais", icon="2️⃣")
    st.page_link("pages/03_Banco de Dados.py", label="Banco de dados de águas minerais", icon="3️⃣")

    st.divider()

    st.write('## Conversor rápido de alcalinidade para bicarbonato')
    bicarbonato = float(st.number_input("Bicarbonato (mg/L):", value=100.0, step=5.0, key='bicarbonato_rapido'))

    alcalinidade = converte_alcalinidade_bicarbonato(bicarbonato)

    st.success(f"Alcalinidade equivalente: {alcalinidade:.2f} ppm")