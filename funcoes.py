# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------
# Created By  : Gilmar Ceregato
# Created Date: 22/02/2025
# Changed Date: 12/07/2025
# version ='1.1'
# ----------------------------------------------------------------------
# Funções para o cálculo de águas para café
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
# ----------------------------------------------------------------------
__author__ = 'Gilmar Ceregato' 
__copyright__ = 'Copyright 2025, Calculadora Águas para Café' 
__credits__ = ['Thiago Motta (thiagomottaas)',] 
#credits inclui as pessoas que reponrtaram bugs, fizeram sugestões, etc, mas que não escreveram o código. 
__email__ = 'gilceregato@gmail.com' 
__status__ = 'Development' # (Prototype, Development or Production)
# ----------------------------------------------------------------------
# Funções 
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