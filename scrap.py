# -*- coding: utf-8 -*-
"""
Created on Mon Sep 1 07:05:40 2019

@authors: Hernán & Elvis
"""


from selenium import webdriver

import re
import os


import selenium.webdriver.support.ui as UI
from random import randint
from time import sleep
import datetime

import buscar_contrato
import datos_contrato
import descargar_docs
import formatt
import siguiente_pagina as sp

solo_contratos = [] #Lista de contratos
solo_licitacion = [] 

def loop_page(driver, nombres_licitacion, etapas_licit, year, path):
    for i, etapa in enumerate(etapas_licit):
  
        if etapa.text == 'Adjudicada':
            #enter to the licitacion
            enlace = nombres_licitacion[i].get_attribute('href')
            driver.execute_script("window.open('');")
            driver.switch_to.window(driver.window_handles[1])
            driver.get(enlace)
            sleep(3)

            contrato_out = datos_contrato.obtener_datos(driver)
            
            contrato_out.update({'periodo':int(year)})
            
            contrato_out = formatt.main(contrato_out)
            
            #Download files and get total amount.
            contrato_out, again = descargar_docs.main(driver, year, path,  contrato_out)

            while again:
                print("---I entered here---")
                #Download files and get total amount, in case error ocurred
                contrato_out, again = descargar_docs.main(driver, year, path,  contrato_out)

            #Formatting Monto Adjudicado and monto total
            try:
                
                contrato_out['monto_ampliacion'] = int(contrato_out['monto_ampliacion'][2:].replace(".", "").replace(",", ""))
                
            except ValueError:
                
                contrato_out['monto_ampliacion'] = 0
            solo_contratos.append(contrato_out)

            driver.close()
            driver.switch_to.window(driver.window_handles[0])

def main(municipio = "Hernandarias", year = datetime.datetime.now().year):
    #Convocante de las licitaciones
    year = str(year)
    convocante = 'Municipalidad de '+ municipio

    ###### Change Download folder
    path = "{}\\Temps{}\\{}".format(os.getcwd(), municipio, year)
    if  not os.path.exists(path):
        os.makedirs(path)

    chrome_options = webdriver.ChromeOptions()
    prefs = {'download.default_directory' : path}
    chrome_options.add_experimental_option('prefs', prefs)
    driver = webdriver.Chrome(options=chrome_options)
    #wait until "Busqueda Avanzada" button is available
    sleep(0.5)

    wait = UI.WebDriverWait(driver, 5000)


    web_url = 'https://www.contrataciones.gov.py/buscador/contratos.html'
    driver.get(web_url)
    sleep(2)



    buscar_contrato.buscar_contrato(convocante, year, driver)


        
    ### Resultado de busqueda
    xp_nombres_licit = '//*[@id="contratos"]/ul/li/article/header/h3/a'
    xp_etapas_licit = '//*[@id="contratos"]/ul/li/article/div/div[1]/div[1]/div[2]/em'
    nombres_licitacion = driver.find_elements_by_xpath(xp_nombres_licit)
    etapas_licit = driver.find_elements_by_xpath(xp_etapas_licit)
    loop_page(driver, nombres_licitacion, etapas_licit, year, path)



    #Is there a next page? If so, go for it
    xp_pagination = '//*[@id="contratos"]/div[2]/div/div[2]/div/ul'
    while sp.siguiente_pag(driver, xp_pagination):
        try:
            nombres_licitacion =  driver.find_elements_by_xpath(xp_nombres_licit)
            etapas_licit =  driver.find_elements_by_xpath(xp_etapas_licit)

            loop_page(driver, nombres_licitacion, etapas_licit, year, path)
            
        except Exception as e:
            print(e)
            print("En cristiano: Posiblemente no hay segunda pagina")

        

        
    
    driver.close()
    len(solo_contratos)
    return solo_contratos

if __name__ == '__main__':

    datos = main()

