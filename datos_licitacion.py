# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 11:24:05 2019

@author: Hernán
"""

import os
import re
import down_utils
import selenium.webdriver.support.ui as UI
from random import randint
from time import sleep    


def obtener_datos(driver):
    wait = UI.WebDriverWait(driver, 5000) #Capaz pasar a otra parte

    #driver.switch_to.window(ventana)
    #print(driver.title)
    xp_ul_steps = '/html/body/div[2]/div[2]/ul'
    ul_steps = driver.find_element_by_xpath(xp_ul_steps)
    step = ul_steps.find_element_by_class_name("active").text.lower()
    step = step.replace('ó','o')
    
    if step == 'adjudicacion':
        datos={
        'id_licitacion' : '//*[@id="datos_' + step + '"]/section/div/div/div[1]/div[2]/em',
        'nombre_licitacion' : '//*[@id="datos_' + step + '"]/section/div/div/div[2]/div[2]/em',
        'convocante' : '//*[@id="datos_' + step + '"]/section/div/div/div[3]/div[2]',
        'estado' : '//*[@id="datos_' + step + '"]/section/div/div/div[7]/div[2]/em',
        'monto' : '//*[@id="datos_' + step + '"]/section/div/div/div[9]/div[2]',
        'fecha_publicacion' : '//*[@id="datos_' + step + '"]/section/div/div/div[10]/div[2]',
        'sistema_adjudicacion' : '//*[@id="datos_' + step + '"]/section/div/div/div[8]/div[2]',
        }
    elif step == 'convocatoria':
        datos={
        'id_licitacion' : '//*[@id="datos_' + step + '"]/section[1]/div/div/div[1]/div[2]/em',
        'nombre_licitacion' : '//*[@id="datos_' + step + '"]/section[1]/div/div/div[1]/div[4]/em',
        'convocante' : '//*[@id="datos_' + step + '"]/section[1]/div/div/div[2]/div[2]',
        'estado' : '//*[@id="datos_' + step + '"]/section[1]/div/div/div[5]/div[2]/em',
        'monto' : '//*[@id="datos_' + step + '"]/section[1]/div/div/div[4]/div[2]',
        'fecha_publicacion' : '//*[@id="datos_' + step + '"]/section[1]/div/div/div[5]/div[4]',
        'sistema_adjudicacion' : '//*[@id="datos_' + step + '"]/div[3]/div[1]/section/div/div/div[1]/div[2]',
        #'sistema_adjudicacion' : '//*[@id="datos_' + step + '"]/section/div/div/div[8]/div[2]',
        }
    elif step == 'planificacion':
        datos={
        'id_licitacion' : '//*[@id="datos_' + step + '"]/section[1]/div/div/div[1]/div[2]/em',
        'nombre_licitacion' : '//*[@id="datos_' + step + '"]/section[1]/div/div/div[1]/div[4]/em',
        'convocante' : '//*[@id="datos_' + step + '"]/section[1]/div/div/div[2]/div[2]',
        'estado' : '//*[@id="datos_' + step + '"]/section[1]/div/div/div[5]/div[2]/em',
        'monto' : '//*[@id="datos_' + step + '"]/div[3]/div[1]/section/div/div/div[1]/div[2]',
        'fecha_publicacion' : '//*[@id="datos_' + step + '"]/section[1]/div/div/div[5]/div[4]',
        #'sistema_adjudicacion' : '//*[@id="datos_' + step + '"]/section[1]/div/div/div[4]/div[2]',
        #'sistema_adjudicacion' : '//*[@id="datos_' + step + '"]/section/div/div/div[8]/div[2]',
        }    
    
    licitacion = {} 
    for key in datos:
        try:
            info = driver.find_element_by_xpath(datos[key]).text
            licitacion.update({key:info})
        except:
            licitacion.update({key:''})
            pass
    
    return(licitacion)
    #print(licitacion)
    #solo_licitacion.append(licitacion)


        ###### Lo que se extrae de la página de licitaciones



        ####### Se navega la pestaña de Convocatoria
#        xp_link_convocatoria = '/html/body/div[2]/div[2]/ul/li[2]/a'
#        driver.find_element_by_xpath(xp_link_convocatoria).click() #Hacer click en convocatoria
    
        ##### Se crea una carpeta con el nombre de la ciudad (convocante) para guardar archivos
        #make_sure_path_exists(convocante)
    
        ### Se extra el sistema de adjudicacion
#        xp_sistema_adjudicacion = '//*[@id="datos_convocatoria"]/div[3]/div[1]/section/div/div/div[1]/div[2]'
        #if sistema adjudicacion == Por lote, entonces guardar lista de lotes
    
        ##### En caso true se navega a la lista de items solicitados para guardar la lista
#        xp_items_solicitados = '/html/body/div[2]/ul/li[3]/a'
#        driver.find_elements_by_xpath(xp_items_solicitados).click()
#        xp_lotes = '//*[@id="itemSolicitados"]/div/div[1]/aside/div/ul/li/a'
#    
#        #### Se navega a la carpeta de documentos para descargar el pliego de B y C
#        xp_documentos_convocatoria = '/html/body/div[2]/ul/li[4]/a'
#        driver.find_element_by_xpath(xp_documentos_convocatoria).click()
#        
#        ### Hay iterar sobre la tabla para encontrar el pliego y despues decargar, sino pasar a la pag 2    
#        xp_checkbox_condiciones = '//*[@id="checkboxSeccionesEstandares"]'
#        driver.find_element_by_xpath(xp_checkbox_condiciones).click()
#    
#        table_id = driver.find_element_by_tag_name('tbody')
#        rows = table_id.find_elements_by_tag_name("tr") # get all of the rows in the table
#    
#        for row in rows:
#            # Get the columns (all the column 2)        
#            #col = row.find_elements(By.TAG_NAME, "td")[1] #note: index start from 0, 1 is col 2
#            #print col.text #prints text from the element
#            col = row.find_elements_by_tag_name("td")[0]
#            if col.text == 'Pliego de bases y Condiciones':
#                print(row.text)
    
        #Pasar a la página 2 de la tabla de documentos
#        xp_pagina2 = '//*[@id="documentos"]/div[2]/div[2]/div[2]/div/ul/li[3]/a'
#        driver.find_element_by_xpath(xp_pagina2).click()
#       
#        cols = row.find_elements_by_tag_name("td")
#        link = cols[3].find_element_by_tag_name("a")
#        link.click()
  
        ### Navegar a la pestaña de invitados en caso de que existan
#        xp_invitados = '/html/body/div[2]/ul/li[6]/a'
    
        ### Navegar a adjudicacion
        #Aca ya tengo xpaths al comienzo
        
        ##Navegar a oferentes presentados
#        xp_oferentes_presentados = '/html/body/div[2]/ul/li[4]/a'
        #guardar lista de oferentes presentados
        
