# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 17:39:21 2019

@author: Hernán
"""

#import csv
#from time import sleep, strftime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.support.ui import Select
#from random import randint
import pandas as pd
#import numpy
#import re
import buscar_licitacion

import time
import os

import datos_contrato

###### Change Download folder
chrome_options = webdriver.ChromeOptions()
prefs = {'download.default_directory' : os.getcwd() + '\\Downloads'}
chrome_options.add_experimental_option('prefs', prefs)
driver = webdriver.Chrome(chrome_options=chrome_options)


chrome_path = r"chromedriver.exe"
driver = webdriver.Chrome(chrome_path)
web_url = 'https://www.contrataciones.gov.py/buscador/licitaciones.html'
driver.get(web_url)

convocante = 'Municipalidad de Ciudad del Este'

buscar_licitacion(convocante)


### Resultado de busqueda
xp_nombres_licit = '//*[@id="licitaciones"]/ul/li/article/header/h3/a'
xp_etapas_licit = '//*[@id="licitaciones"]/ul/li[2]/article/div/div[1]/div[1]/div[2]/em'
nombres_licitacion = driver.find_elements_by_xpath(xp_nombres_licit)
etapas_licit = driver.find_elements_by_xpath(xp_etapas_licit)

## Hacer esto cada vez que se vuelve a la lista de resultados
i = 0 #para iterar sobre resultados en nombres
for i, etapa in enumerate(etapas_licit):
    if etapa.text == 'Adjudicada':
        nombres_licitacion[i].click()

        ###### Lo que se extrae de la página de licitaciones
        xp_id_licitacion = '//*[@id="datos_adjudicacion"]/section/div/div/div[1]/div[2]/em'
        xp_nombre_licitacion = '//*[@id="datos_adjudicacion"]/section/div/div/div[2]/div[2]/em'
        xp_estado = '//*[@id="datos_adjudicacion"]/section/div/div/div[7]/div[2]/em'
        xp_monto = '//*[@id="datos_adjudicacion"]/section/div/div/div[9]/div[2]'
        xp_fecha_publicacion = '//*[@id="datos_adjudicacion"]/section/div/div/div[10]/div[2]'
    
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
        
#        #Navegar a proveedores adjudicados
#        Iterar sobre tabla con empresas adjudicadas
#        Hacer click en ver contrato
#        Descargar: CC
        
        solo_contratos = []
        contrato_out = datos_contrato.obtener_datos(driver)
        solo_contratos.append(contrato_out)
        
        driver.execute_script("window.history.go(-1)")
        sleep(randint(10,15))
        
        
        #Navegar a documentos
        #Descargar "Orden de Compra o Contrato"
        
        
    
    else:







    




el.text
out = map(lambda x: x.text, el)
lista = list(out)


