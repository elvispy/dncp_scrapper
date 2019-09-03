# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 17:39:21 2019

@author: Hernán
"""

#import csv
#from time import sleep, strftime
from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.support.ui import Select
#from random import randint
import pandas as pd
#import numpy
import re
import os
#import time

import selenium.webdriver.support.ui as UI
from random import randint
from time import sleep

import buscar_licitacion
import datos_contrato
import datos_licitacion

###### Change Download folder
chrome_options = webdriver.ChromeOptions()
prefs = {'download.default_directory' : os.getcwd() + '\\Downloads'}
chrome_options.add_experimental_option('prefs', prefs)
driver = webdriver.Chrome(options=chrome_options)


wait = UI.WebDriverWait(driver, 5000)


web_url = 'https://www.contrataciones.gov.py/buscador/licitaciones.html'
driver.get(web_url)
sleep(randint(5,10))


year = '2018'
municipio = "Hernandarias"
convocante = 'Municipalidad de '+ municipio
buscar_licitacion.buscar_licitacion(convocante, driver)
solo_contratos = [] #Lista de contratos
solo_licitacion = [] 
### Iterar sobre los resultados en licitaciones
existe_siguiente_pagina = True
while existe_siguiente_pagina == True:
    existe_siguiente_pagina = False
    
### Resultado de busqueda
xp_nombres_licit = '//*[@id="licitaciones"]/ul/li/article/header/h3/a'
xp_etapas_licit = '//*[@id="licitaciones"]/ul/li/article/div/div[1]/div[1]/div[2]/em'
nombres_licitacion = driver.find_elements_by_xpath(xp_nombres_licit)
etapas_licit = driver.find_elements_by_xpath(xp_etapas_licit)

## Hacer esto cada vez que se vuelve a la lista de resultados
#i = 0 #para iterar sobre resultados en nombres
for i, etapa in enumerate(etapas_licit):
    print(i)
    print(etapa)
    print(etapa.text)
    if etapa.text == 'Adjudicada':
        enlace = nombres_licitacion[i].get_attribute('href')
        driver.execute_script("window.open('');")
        driver.switch_to.window(driver.window_handles[1])
        driver.get(enlace)
        sleep(randint(5,10))


        licitacion_out = datos_licitacion.obtener_datos(driver)
        solo_licitacion.append(licitacion_out)
        #dff = pd.DataFrame(solo_licitacion, columns=['id_licitacion', 'nombre_licitacion', 'fecha_publicacion', 'estado', 'monto', 'sistema_adjudicacion'])
        #dff.to_csv(os.getcwd() + '\\solo_lic.csv', encoding='utf-8',index=False)
        
        #Navegar a proveedores adjudicados
        xp_ul_tabs = '/html/body/div[2]/ul'
        ul_tabs = driver.find_element_by_xpath(xp_ul_tabs)
        ul_tabs.find_element_by_link_text("Proveedores Adjudicados").click()
        
        #def downl_from_table(down):
        table_id = wait.until(
                lambda driver: driver.find_element_by_tag_name('tbody'))
        
        # get all of the rows in the table
        rows = table_id.find_elements_by_tag_name("tr")
        links_contratos = map(lambda row: row.find_elements_by_tag_name("td")[6].find_element_by_tag_name("a").get_attribute('href'), rows)
        links_contratos = list(links_contratos)
        
        #List Comprehension
        contrato_out = [datos_contrato.entrar_guardar_datos(driver,link) for link in links_contratos]
        solo_contratos.append(contrato_out)

        driver.close()
        driver.switch_to.window(driver.window_handles[0])


df = pd.DataFrame(solo_contratos, columns=['id_licitacion', 'fecha_firma_contrato', 'num_contrato', 'nombre_empresa', 'ruc_empresa', 'monto_adjudicado', 'titulo_contrato', 'municipio', 'codigo_contratacion', 'contrato_download'])
df.to_csv(os.getcwd() + '\\solo_contratos.csv', encoding='utf-8',index=False)

