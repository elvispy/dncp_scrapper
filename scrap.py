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
#import pandas as pd
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
driver = webdriver.Chrome(chrome_options=chrome_options)


wait = UI.WebDriverWait(driver, 5000)

#chrome_path = r"chromedriver.exe"
#driver = webdriver.Chrome(chrome_path)
web_url = 'https://www.contrataciones.gov.py/buscador/licitaciones.html'
driver.get(web_url)

convocante = 'Municipalidad de Ciudad del Este'

buscar_licitacion.buscar_licitacion(convocante, driver)


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
        sleep(randint(2,5))
        #En pag licitación, hacer algo
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        #print("Current Page Title is : %s" %driver.title)


        break

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
            col = row.find_elements_by_tag_name("td")[6]
            link = col.find_element_by_tag_name("a").get_attribute('href')
           
            driver.execute_script("window.open('');")
            driver.switch_to.window(driver.window_handles[2])
            driver.get(link)
            sleep(randint(2,5))
            
            solo_contratos = []
            contrato_out = datos_contrato.obtener_datos(driver)
            solo_contratos.append(contrato_out)
                
            driver.close()
            driver.switch_to.window(driver.window_handles[1])
            
            
            
            print('test')
            if col.text == 'Orden de Compra o Contrato':
                contrato_down = True
                cols = row.find_elements_by_tag_name("td")
                link = cols[3].find_element_by_tag_name("a")
                link.click()
                break
    
    if contrato_down == True:
        directory = 'Downloads' #Carpeta default para descargar archivos. Configurado también al inciar Selenium
        contrato_down = down_utils.wait_rename(dest_path, directory, timeout = 30)
        contrato.update({'contrato_download' : contrato_down})
    else:
        contrato.update({'contrato_download' : False})
        
        
        
        tab_url = 'https://www.contrataciones.gov.py/licitaciones/adjudicacion/contrato/355675-isabel-petrona-gomez-cabrera-2.html'
        driver.execute_script("window.open('');")
        driver.switch_to.window(driver.window_handles[1])
        driver.get(tab_url)
        #En pag contrato, hacer algo
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        print("Current Page Title is : %s" %driver.title)
        
        
        #etapas_licit = driver.find_elements_by_xpath(xp_etapas_licit)
#        Iterar sobre tabla con empresas adjudicadas
#        Hacer click en ver contrato
#        Descargar: CC





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


