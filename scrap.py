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
#import pandas as pd
#import numpy
#import re
import buscar_licitacion

chrome_path = r"chromedriver.exe"
driver = webdriver.Chrome(chrome_path)
web_url = 'https://www.contrataciones.gov.py/buscador/licitaciones.html'
driver.get(web_url)

convocante = 'Municipalidad de Ciudad del Este'

buscar_licitacion(convocante)

