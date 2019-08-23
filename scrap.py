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
#import re
import os
#import time

import selenium.webdriver.support.ui as UI
from random import randint
from time import sleep

import buscar_licitacion
import datos_contrato

###### Change Download folder
chrome_options = webdriver.ChromeOptions()
prefs = {'download.default_directory' : os.getcwd() + '\\Downloads'}
chrome_options.add_experimental_option('prefs', prefs)
driver = webdriver.Chrome(options=chrome_options)


wait = UI.WebDriverWait(driver, 5000)

#chrome_path = r"chromedriver.exe"
#driver = webdriver.Chrome(chrome_path)
web_url = 'https://www.contrataciones.gov.py/buscador/licitaciones.html'
driver.get(web_url)

sleep(randint(5,10))

convocante = 'Municipalidad de Ciudad del Este'

buscar_licitacion.buscar_licitacion(convocante, driver)

solo_contratos = []

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
        #nombres_licitacion[i].click()
        #tab_url = 'https://www.contrataciones.gov.py/licitaciones/adjudicacion/contrato/355675-isabel-petrona-gomez-cabrera-2.html'
        enlace = nombres_licitacion[i].get_attribute('href')
        driver.execute_script("window.open('');")
        driver.switch_to.window(driver.window_handles[1])
        driver.get(enlace)
        sleep(randint(5,10))

        #break

#        ###### Lo que se extrae de la página de licitaciones
#        xp_id_licitacion = '//*[@id="datos_adjudicacion"]/section/div/div/div[1]/div[2]/em'
#        xp_nombre_licitacion = '//*[@id="datos_adjudicacion"]/section/div/div/div[2]/div[2]/em'
#        xp_estado = '//*[@id="datos_adjudicacion"]/section/div/div/div[7]/div[2]/em'
#        xp_monto = '//*[@id="datos_adjudicacion"]/section/div/div/div[9]/div[2]'
#        xp_fecha_publicacion = '//*[@id="datos_adjudicacion"]/section/div/div/div[10]/div[2]'

#        #Navegar a proveedores adjudicados
        xp_proveedores_adjudicados = '/html/body/div[2]/ul/li[3]/a'
        driver.find_element_by_xpath(xp_proveedores_adjudicados).click()
        
        #def downl_from_table(down):
        table_id = wait.until(
                lambda driver: driver.find_element_by_tag_name('tbody'))
        # get all of the rows in the table
        rows = table_id.find_elements_by_tag_name("tr") 
        for row in rows:
            col_acciones = row.find_elements_by_tag_name("td")[6]
            link_contrato = col_acciones.find_element_by_tag_name("a").get_attribute('href')
           
            driver.execute_script("window.open('');")
            driver.switch_to.window(driver.window_handles[2])
            driver.get(link_contrato)
            sleep(randint(5,10))
            
            
            contrato_out = datos_contrato.obtener_datos(driver)
            solo_contratos.append(contrato_out)
                
            driver.close()
            driver.switch_to.window(driver.window_handles[1])
       
        #etapas_licit = driver.find_elements_by_xpath(xp_etapas_licit)
#        Iterar sobre tabla con empresas adjudicadas
#        Hacer click en ver contrato
#        Descargar: CC

        driver.close()
        driver.switch_to.window(driver.window_handles[0])



#        
#        driver.execute_script("window.history.go(-1)")
#        sleep(randint(10,15))
#        
#        
#        #Navegar a documentos
#        #Descargar "Orden de Compra o Contrato"
#        
#        
#    
#    else:
#
#
#
#
#
#
#
#    
#
#
#
#
#el.text
#out = map(lambda x: x.text, el)
#lista = list(out)

df = pd.DataFrame(solo_contratos, columns=['id_licitacion', 'fecha_firma_contrato', 'num_contrato', 'nombre_empresa', 'ruc_empresa', 'monto_adjudicado', 'titulo_contrato', 'municipio', 'codigo_contratacion', 'contrato_download'])
df.to_csv(os.getcwd() + '\\solo_contratos.csv', encoding='utf-8',index=False)