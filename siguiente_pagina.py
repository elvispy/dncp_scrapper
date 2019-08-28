# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 19:19:13 2019

@author: Hernán
"""
import re
from time import sleep


def siguiente_pag_licitacion(driver):
    try:
        xp_ul_paginas = '//*[@id="licitaciones"]/div[2]/div/div[2]/div/ul'
        uls = driver.find_element_by_xpath(xp_ul_paginas)
        lis = uls.find_elements_by_tag_name("li")
        
        pagina_activa = uls.find_element_by_class_name("active").text #da la página activa
        pagina_activa = re.search("\d+", pagina_activa).group(0)
        
        ultima_pagina = lis[-2].text
        ultima_pagina = re.search("\d+", ultima_pagina).group(0)
        
        if pagina_activa != lis[-2].text:
            lis[-1].find_element_by_tag_name("a").click() #hacer click en siguiente pagina
            sleep(3)
            print('La página activa es: ' + pagina_activa)
            print('La última página es: ' + ultima_pagina)
            existe_siguiente_pagina = True
    except:
        existe_siguiente_pagina = False
        pass
    return existe_siguiente_pagina