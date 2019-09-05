import scrap

import xlstodrive

import formatt

import savetojson

<<<<<<< HEAD
year = 2016
=======
year = 2014

>>>>>>> f93b08ad5d2cc13544fe3bc83a76df5ee963181a
municipio = 'Hernandarias'
scrap_var = True #Want to scrap th website?
up_to_cloud = False #Want to upload the data to drive?

<<<<<<< HEAD
def main(scrap_var = True, up_to_cloud = True):
=======
#This exception lists is in case there is a case my code can't handle, so it
# can skip it write the id and the number of the contract
exceptions = ['283191 44/2014']

def main():
>>>>>>> f93b08ad5d2cc13544fe3bc83a76df5ee963181a

    #The check if there is an error here first (It's likely that that's the case)
    xlstodrive.checkcredentials()

<<<<<<< HEAD
    
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
=======
    datos = scrap.main(municipio, year)

    savetojson.main(datos)

    #import json
    
    #datos = json.load(open("data.json"))

    #datos = list(datos.values())
    
    xlstodrive.main(datos, year, exceptions)

    return datos

if __name__ == '__main__':

    datos = main()
>>>>>>> f93b08ad5d2cc13544fe3bc83a76df5ee963181a
