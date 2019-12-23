import os

import selenium.webdriver.support.ui as UI

from selenium import webdriver

from time import sleep

import glob

import PyPDF2

import PBC



def find_proveedor(rows, datos):
    name = datos['proveedor'].lower().split(" ")

    for element in rows:
        prov_name = element.find_element_by_tag_name("td").text.lower()
        
        if name[0] in prov_name:
            return element
        
    return None

def move_to_download_folder(downloadPath, fileDestination,  newFileName, fileExtension):
    ''' This function moves all downloaded files to their corresponding ones'''
    
    if os.path.isfile(fileDestination+newFileName+fileExtension):
        files = glob.glob(downloadPath+"\\*"+fileExtension)
        for file in files:
            os.remove(file)
        return None

    got_file = False   
    ## Grab current file name.
    while got_file == False:
        try: 
            currentFile = glob.glob(downloadPath+"\\*"+fileExtension)[0]
        
            got_file = True
            

        except Exception as e:
            pass
            #print(e)
            #print ("File has not finished downloading")
            sleep(2)

    ## Create new file name
    
    fileDestination = fileDestination+newFileName+fileExtension
   
    os.rename(currentFile, fileDestination)

    
    sleep(1)

def documentos_tab(driver):
    wait = UI.WebDriverWait(driver, 5000)
    xp_ul_tabs = '/html/body/div[2]/ul'
    ul_tabs = driver.find_element_by_xpath(xp_ul_tabs)
    try:
        ul_tabs.find_element_by_link_text("Documentos").click()
        sleep(2)

        #wait until the table charges:
        table_id = wait.until(
            lambda driver: driver.find_element_by_tag_name('tbody'))
        #Get all rows
        rows = table_id.find_elements_by_tag_name("tr")
        #get the correct row
        row = [element for element in rows
           if ("contrato" in
               element.find_element_by_tag_name("td").text.lower() )][0]
        return row
        
    except Exception as e:
        print(e)
        return None

def ampliaciones_tab(driver, datos):
    
    wait = UI.WebDriverWait(driver, 5000)
    xp_ul_tabs = '/html/body/div[2]/ul'
    ul_tabs = driver.find_element_by_xpath(xp_ul_tabs)

    link_to_cc = ""
    try:
        ul_tabs.find_element_by_link_text("Modificaciones al Contrato").click()

        sleep(2)

        #wait until the table charges:
        table_id = wait.until(
            lambda driver: driver.find_element_by_tag_name('tbody'))
        #Get all rows
        #rows = table_id.find_elements_by_tag_name("tr")
        xp_table = '//*[@id="modificaciones"]/div/div[1]/table/tbody/tr'
        rows = driver.find_elements_by_xpath(xp_table)
 
        row = [element for element in rows
           if ("monto" in element.find_element_by_tag_name("td").text.lower() )][0]
   
        monto_ampliacion = row.find_elements_by_tag_name("td")[-3].text
        datos.update({'monto_ampliacion':monto_ampliacion})

        link_to_cc = row.find_elements_by_tag_name("td")[-1].find_element_by_tag_name("a").get_attribute('href')
   
        return  link_to_cc

    except Exception as e:
        datos.update({'monto_ampliacion':''})
        #print("------------------")
        #print(e)
        #print("------------------")
        
        return  ""

        

        

def main(driver, year, path, datos):
    wait = UI.WebDriverWait(driver, 5000) #Capaz pasar a otra parte
    #Check for the table of the contract
    xp_ul_tabs = '/html/body/div[2]/ul'

    #To avoid errors caused by moving the browser
    row = documentos_tab(driver)
    while row is None:
        row = documentos_tab(driver)

    #Create folders to store the documents
    nomenclatura = "{nro} {id_c} {name}".format(
        nro = datos['nro_contrato'].replace("/", "-"),
        id_c = datos['id_licitacion'],
        name = datos['nombre_empresa']
        )
    if  not os.path.exists(path + "\\" + nomenclatura):
        os.makedirs(path + "\\" + nomenclatura)

    
    #Download contract, if it's not already on the pc
    if os.path.isfile(path + "\\" + nomenclatura + "\\Contrato " + datos['nombre_empresa'] + ".pdf"):
        pass
    else:
        row.find_elements_by_tag_name("td")[-1].find_element_by_tag_name("a").click()
    
        #Move contract to correct folder
        move_to_download_folder(path, path + "\\" + nomenclatura + "\\",
                            "Contrato " + datos['nombre_empresa'],
                            ".pdf")

    #See if there are ampliaciones and return the downloadable link
    link_to_cc  = ampliaciones_tab(driver, datos)

    #Download if there is one ampliation
    if bool(link_to_cc) and not os.path.isfile("{}//{}//Ampliacion (CC).pdf".format(path, nomenclatura)):

        driver.execute_script("window.open('');")

        driver.switch_to.window(driver.window_handles[2])

        driver.get(link_to_cc)

        xp_relacionados = '//*[@id="datos_modificaciones_contrato"]/div/div/div/ul'

        driver.find_element_by_link_text("Descargar Código de Contratación (CC)").click()

        sleep(1)

        move_to_download_folder(path, "{}\\{}\\".format(path, nomenclatura),
                            "Ampliacion (CC)",
                            ".pdf")
        sleep(0.5)
        driver.close()
        driver.switch_to.window(driver.window_handles[1])
        sleep(0.1)


        

    #Buscando el codigo de contratacion

    xp_back_to_convocatoria = '/html/body/div[2]/div[2]/ul/li/a'
    driver.find_element_by_xpath(xp_back_to_convocatoria).click()
    sleep(2)
    #Update monto total
    xp_monto_total = '//*[@id="datos_adjudicacion"]/section/div/div/div[9]/div[2]'
    monto_total = driver.find_element_by_xpath(xp_monto_total).text
    datos.update({'monto_total':monto_total})
    datos['monto_total'] = int(datos['monto_total'][2:].replace(".", ""))

    
    #ver si se puede hacer mas corto
    if os.path.isfile(path + "\\" + nomenclatura + "\\Codigo de Contratacion.pdf"):
        pass
    else:
        
    
        #Click to Proveedores adjudicados
        ul_tabs = driver.find_element_by_xpath(xp_ul_tabs)
        ul_tabs.find_element_by_link_text("Proveedores Adjudicados").click()

        #wait until the table charges:
        table_id = wait.until(
            lambda driver: driver.find_element_by_tag_name('tbody'))

        
        #Get all rows
        rows = table_id.find_elements_by_tag_name("tr")

        row_proveedor = find_proveedor(rows, datos)
        c = 1
        while row_proveedor is None:
            print("Beware, html element not found. Retrying...")
            print(c)
            print("--------")
            c+=1
            sleep(2)
            rows = table_id.find_elements_by_tag_name("tr")

            row_proveedor = find_proveedor(rows, datos)

        sleep(0.1)
        #Download Codigo de Contratacion
        down_button = row_proveedor.find_elements_by_tag_name("td")[-1]
    
        #row_proveedor.find_element_by_tag_name("div").find_elements_by_tag_name("a")[-1].click()
        sleep(0.1)
        enlace = down_button.find_element_by_tag_name("ul").find_element_by_tag_name("li").find_element_by_tag_name("a").get_attribute('href')

        driver.execute_script("window.open('');")
        driver.switch_to.window(driver.window_handles[2])
        driver.get(enlace)

    
        move_to_download_folder(path, "{}\\{}\\".format(path, nomenclatura),
                            "Codigo de Contratacion",
                            ".pdf")
    
        driver.close()
        driver.switch_to.window(driver.window_handles[1])



    error = False
    monto_fonacide = "-1"
    try:
        pdfFile = open(path + "\\" + nomenclatura + "\\Codigo de Contratacion.pdf", 'rb')

        pdfObject = PyPDF2.PdfFileReader(pdfFile)

        pdfPage = pdfObject.getPage(0)

        monto_fonacide = pdfPage.extractText().split("TOTAL:")[1]
        
        if pdfPage.extractText().split("TOTAL:")[0][-len(monto_fonacide):] != monto_fonacide:
            print("Warning: Check Possible Error in Monto Fonacide (PDF) didn't match:")
            print(datos['id_licitacion'])
            print(datos['nro_contrato'])
            print("File descargar_docs.py, line 265")
            print("--------------------")
            monto_fonacide = '-1'
        elif pdfPage.extractText().split("TOTAL:")[0][-len(monto_fonacide)-3] != '3':
            monto_fonacide = '0'
    except:

        error = True
    datos.update({'monto_fonacide':int(monto_fonacide.replace(",", ""))})



    #check if there is an ampliacion
    monto_ampliacion_fon = "0"
    if link_to_cc:
        try:
            pdfFile = open(path + "\\" + nomenclatura + "\\Ampliacion (CC).pdf", 'rb')

            pdfObject = PyPDF2.PdfFileReader(pdfFile)

            pdfPage = pdfObject.getPage(0)

            monto_ampliacion_fon = pdfPage.extractText().split("TOTAL:")[1]
            if monto_ampliacion_fon[-1] == " ":
                monto_ampliacion_fon= monto_ampliacion_fon[:-1]
        
            if pdfPage.extractText().split("TOTAL:")[0][-len(monto_ampliacion_fon):] != monto_ampliacion_fon:
                print(pdfPage.extractText().split("TOTAL:")[0][-len(monto_ampliacion_fon):])
                print(monto_ampliacion_fon)
                print("Warning: Check Possible Error in Ampliacion:")
                print(datos['id_licitacion'])
                print(datos['nro_contrato'])
                print("--------------------")
            elif pdfPage.extractText().split("TOTAL:")[0][-len(monto_ampliacion_fon)-3] != '3':
                monto_ampliacion_fon = '0'
        except Exception as e:
            print(e)
    datos.update({'monto_fonacide':
                  datos['monto_fonacide']+ int(monto_ampliacion_fon.replace(",", ""))})

    #Try to download PBC

    #Has the PBC already been downloaded?
    if not (os.path.isfile("{}\\{}\\Pliego de Bases y Condiciones {}.pdf".format(
        path, nomenclatura, datos['nro_contrato'].replace("/", "-"))) or
            os.path.isfile("{}\\{}\\Pliego de Bases y Condiciones {}.zip".format(
        path, nomenclatura, datos['nro_contrato'].replace("/", "-"))) or
            os.path.isfile("{}\\{}\\Pliego de Bases y Condiciones {}.docx".format(
        path, nomenclatura, datos['nro_contrato'].replace("/", "-")))):

        #Download and get extension
        PBC_down, pliego_extension = PBC.PBC(driver)
        

        if PBC_down:
            #print("{}\\{}\\".format(path, nomenclatura))
            #print(pliego_extension)
            
            move_to_download_folder(path, "{}\\{}\\".format(path, nomenclatura),
                                "Pliego de Bases y Condiciones {}".format(datos['nro_contrato']).replace("/", "-"),
                                pliego_extension)
    

    return [datos, error]
