# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 20:29:19 2019

@author: Hernán
"""

datos={
    'title' : '//*[@id="fullscreen"]/h1', 
    'fast_facts' : '#facts',
    'strengths' : '/html/body/div[1]/section[4]/div/div/div[1]/ul',
    'ratings' : '/html/body/div[1]/section[4]/div/div/div[2]',
    'fact_sheet' : '/html/body/div[1]/section[2]/div/div/div[2]/div/a[2]',
}

row_list=[]


def page_scrape():
    dictio = {}
    for key in datos:
        if key=='fast_facts':
            location_text = driver.find_element_by_css_selector(datos[key]).text
            dictio.update({key:location_text})
        elif key=='fact_sheet':
            try:
                info = driver.find_element_by_xpath(datos[key]).get_attribute('href')
                dictio.update({key:info})
            except:
                dictio.update({key:''})
                pass
        else:
            try:
                info = driver.find_element_by_xpath(datos[key]).text
                dictio.update({key:info})
            except:
                dictio.update({key:''})
                pass
            
    match = re.search("Location\s*\\n(.*)\\n", dictio['fast_facts'])
    
    if match:
        result = match.group(1)
        dictio.update({'location':result})
    else:
        dictio.update({'location':''})
        return(dictio)