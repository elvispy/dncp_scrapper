import json

def main(data):

    data = {"{} {}".format(dato['nro_contrato'], dato['id_licitacion']):
            dato for dato in data}


    try:
        with open("data.json") as f:
            already_charged = json.load(f)
        
        already_charged.update(data)
    except:
        print(e)

    with open("data.json", "w") as json_file:
        
        json.dump(already_charged, json_file, indent = 4, sort_keys = True)


