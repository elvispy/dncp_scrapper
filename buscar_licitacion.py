# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 20:14:29 2019

@author: Hernán
"""
from selenium.webdriver.common.keys import Keys
from time import sleep


def buscar_licitacion(convocante, driver):
    xp_lista_convocantes = '//*[@id="convocantes"]'
    xp_criterios_avanzados = '//*[@id="headingOne"]/h4/a' 
    xp_caract_esp = '//*[@id="collapseOne"]/div/div[1]/div/span[1]/span[1]/span/ul/li/input'
    xp_buscar = '//*[@id="btn_buscar"]' 

    
    lista_convocantes = driver.find_element_by_xpath(xp_lista_convocantes)
    
    for option in lista_convocantes.find_elements_by_tag_name('option'):
        if option.text == convocante:
            option.click() 
            break
        
    driver.find_element_by_xpath(xp_criterios_avanzados).click()
    sleep(0.5)
    driver.find_element_by_xpath(xp_caract_esp).send_keys("Fonacide", Keys.RETURN)
    driver.find_element_by_xpath(xp_buscar).click()