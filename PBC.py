import siguiente_pagina as sp
import selenium.webdriver.support.ui as UI

from time import sleep




def PBC(driver):
    """ 
    Navega a la pestaña convocatoria y descarga el archivo de PBC
  
    Navega a la pestaña convocatoria y descarga el archivo de Pliego de
    Bases y Condiciones. Guarda en la carpeta:
        Temps(Municipio)/Año/NomenclaturaCarpeta/Pliego de Bases y Condiciones
    
    Parameters: 
    driver (WebDriver Object): Driver de selenium
    
  
    Returns: 
    PDC_down: Boolean indicando si se ha encontrado el pliego de bases y condiciones
    pliego_extension: indicador de la extension del archivo para manejarlo correctamente al
    transferir a otra carpeta
  
    """

    #### Se navega a la carpeta de documentos para descargar el pliego de B y C
    # ************      Cambiar para buscar por nombre de la pestaña (documentos)
    
    wait = UI.WebDriverWait(driver, 50) #Capaz pasar a otra part
    xp_ul_steps = '/html/body/div[2]/div[2]'
    xp_ul_tabs = '/html/body/div[2]/ul'
    try:
        ul_steps = driver.find_element_by_xpath(xp_ul_steps) 
        ul_steps.find_element_by_link_text("Convocatoria").click()
        ul_tabs = driver.find_element_by_xpath(xp_ul_tabs) #xp definido al inicio
        ul_tabs.find_element_by_link_text("Documentos").click() 
    except:
        print(e)
        pass


    ##----------------- Tabla
    existe_siguiente_pagina = True
    PBC_down = False
    pliego_extension = None
    while existe_siguiente_pagina:
        sleep(3)
        table_id = wait.until(lambda driver: driver.find_element_by_tag_name('tbody'))
        rows = table_id.find_elements_by_tag_name("tr") # get all of the rows in the table
        for row in rows:
            cols = row.find_elements_by_tag_name("td") # Get the columns
            if cols[0].text == 'Pliego de bases y Condiciones':
                #print('Se encontró el PBC')
                #Hacer click en checkbox
                xp_checkbox_condiciones = '//*[@id="checkboxSeccionesEstandares"]'
                driver.find_element_by_xpath(xp_checkbox_condiciones).click()
 
                cols[-1].find_element_by_tag_name("a").click()

                #Check the file extension to handle it properly
                pliego_extension = cols[-2].text
                pliego_extension = "." + pliego_extension.split(".")[-1]
                
                PBC_down = True
                break
        xp_pagination_PBC = '//*[@id="documentos"]/div[2]/div[2]/div[2]/div/ul'
        existe_siguiente_pagina = sp.siguiente_pag(driver, xp_pagination_PBC)
    return [PBC_down, pliego_extension]
