import scrap

import xlstodrive

import formatt

import savetojson

year = 2016
municipio = 'Hernandarias'
scrap_var = True #Want to scrap th website?
up_to_cloud = False #Want to upload the data to drive?

def main(scrap_var = True, up_to_cloud = True):

    #The check if there is an error here first (It's likely that that's the case)
    xlstodrive.checkcredentials()

    
    if scrap_var:
        datos = scrap.main(municipio, year)
        savetojson.main(datos)

    else:

        import json
        file = open('data.json', 'rb')
        datos = json.load(file)
        datos = list(datos.values())

        
    if up_to_cloud:
        xlstodrive.main(datos, year)

if __name__ == '__main__':

    main(scrap_var, up_to_cloud)
