# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 15:44:30 2019

@author: Hernán
"""

##Lo que se pide en doc reAc:
#No. N° - No hace falta
#No. Año - Se estira de fecha
#Si. N° de contrato
#Si. Empresa
#Si. Fecha de contrato
#Si. Monto total (₲)
#Si. Titulo de contrato
#No. Institución beneficiada
#No. Nº Instituciones beneficiadas
#No. Barrio/Localidad
#No. Monto FONACIDE
#No. Monto Individual (₲)
#No. Puesto en lista de priorización, Aula, Sanitario, Otros espacios
#No. Descripción de obra según título de contrato. 
#
#Guardar:
#    ID de licitacion
#    Fecha de firma de contrato
#    N° de contrato
#    nombre de empresa
#    ruc
#    monto de contrato
#    titulo de contrato





def datos_contrato():
    datos={
    'id_licitacion' : '//*[@id="datos_contrato"]/section[2]/div/div/div[1]/div[2]/em', 
    'fecha_firma_contrato' : '//*[@id="datos_contrato"]/section[1]/div/div/div[4]/div[2]',
    'num_contrato' : '//*[@id="datos_contrato"]/section[1]/div/div/div[3]/div[4]',
    'nombre_empresa' : '//*[@id="datos_contrato"]/section[1]/div/div/div[1]/div[2]/em',
    'ruc_empresa' : '//*[@id="datos_contrato"]/section[1]/div/div/div[1]/div[4]',
    'monto_adjudicado' : '//*[@id="datos_contrato"]/section[1]/div/div/div[3]/div[2]',
    'titulo_contrato' : '/html/body/div[2]/div[1]/h1',
    }
    contrato = {}

    for key in datos:
        try:
          info = driver.find_element_by_xpath(datos[key]).text
          contrato.update({key:info})
        except:
            contrato.update({key:''})
            pass
    return(contrato)
    
    xp_cc = '//*[@id="datos_contrato"]/div[1]/div/div/ul/li[5]/a'
    