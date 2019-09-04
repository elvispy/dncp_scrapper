import scrap

import xlstodrive

import formatt

import savetojson

year = 2014

municipio = 'Hernandarias'

#This exception lists is in case there is a case my code can't handle, so it
# can skip it write the id and the number of the contract
exceptions = ['283191 44/2014']

def main():

    #The check if there is an error here first (It's likely that that's the case)
    xlstodrive.checkcredentials()

    datos = scrap.main(municipio, year)

    savetojson.main(datos)

    #import json
    
    #datos = json.load(open("data.json"))

    #datos = list(datos.values())
    
    xlstodrive.main(datos, year, exceptions)

    return datos

if __name__ == '__main__':

    datos = main()
