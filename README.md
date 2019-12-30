# DNCP-Scrapper V1.0
Python code to scrap DNCP website

If you get an Exception due to some library not installed in your computer, please run setup.bat first, which will install
all libraries needed before compilation.

Also, if you recieve the folowwing exception:
This version of ChromeDriver only supports Chrome version ###
You should probably update your chrome driver version at https://chromedriver.chromium.org/

The current data flow is as follows:

main.py is the central script, it will run all subsequent functions

xlstodrive.checkcredentials()

This line is here because the compilation time is long and this script needs to check the credentials for drive, that's why
its there. You will need to allow at some point use of less secure apps in your google account, since it will  download 
data from google drive and then upload it again as an update.

main.py + year + municipio ---> scrap.py

scrap.py will go trough the DNCP page and get all the necessary data of all contracts, in the following way

scrap.py + selenium driver ---> datos_contrato.py

datos will gather all the information of a single contract and store it in a dictionary

scrap.py + contract data ---> formatt.py

formatt.py will take the dictionary and convert all data to the correct data type (example: str to int if needed)

scrap.py ---> descargar_docs.py

descargar_docs.py will download all files that are required and not in the specified format

scrap.py ---> main.py

Then scrap.py will return a dictionary with data of all contracts

main.py + data ---> savetojson.py

for storing purposes, the dictionary is stored as a json file

main.py + data + year ---> xlstodrive.py

Then the data is passed to xlstodrive, which will download the excel sheet from google drive and write the new data
and alto upload missing files in case they exist.

