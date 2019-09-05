import scrap

import xlstodrive

import formatt

import savetojson

#Settings
year = 2016
municipio = 'Hernandarias'
scrap_var = True #Want to scrap the website?
up_to_cloud = False #Want to upload the data to drive?

#This exception lists is in case there is a case my code can't handle, so it
# can skip it write the id and the number of the contract
exceptions = ['283191 44/2014']


def main(scrap_var = True, up_to_cloud = True):


    #The check if there is an error here first (It's likely that that's the case)
    xlstodrive.checkcredentials()


    #Maybe you already have all the data and just want to 
    if scrap_var:
        datos = scrap.main(municipio, year)
        savetojson.main(datos)

    else:

        import json
        file = open('data.json', 'rb')
        datos = json.load(file)
        datos = list(datos.keys())
        

        
    if up_to_cloud:
        xlstodrive.main(datos, year, municipio)

    return datos

if __name__ == '__main__':

    datos = main(scrap_var, up_to_cloud)


 
