# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 17:44:11 2019

@author: Hernán
"""

#import csv
from time import sleep, strftime
from selenium import webdriver
from random import randint
import pandas as pd
#import numpy
import re

chrome_path = r"C:\python\chromedriver.exe"
driver = webdriver.Chrome(chrome_path)
web_url = 'https://www.inovaeducation.com/en/university-partners/'
driver.get(web_url)


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
    
for i in range(1,36):
    xpath_universidad = '//*[@id="logos"]/div['+str(i)+']/div/a'
    universidad = driver.find_element_by_xpath(xpath_universidad)
    driver.execute_script("arguments[0].click();", universidad)
    sleep(randint(25,35))
    dictionary_outcome = page_scrape()
    row_list.append(dictionary_outcome)
    driver.execute_script("window.history.go(-1)")
    sleep(randint(10,15))
    
df = pd.DataFrame(row_list, columns=['title','location','ratings','strengths','fast_facts','fact_sheet'])
    
df.to_csv('C:\python\Scrap\Lista_Universidades.csv', encoding='utf-8',index=False)