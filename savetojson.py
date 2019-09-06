import json

def main(data, municipio):

    data = {"{} {}".format(dato['nro_contrato'], dato['id_licitacion']):
            dato for dato in data}


    try:
        with open("data{}.json".format(municipio)) as f:
            already_charged = json.load(f)
        
        already_charged.update(data)
    except Exception as e:
        print(e)

    try:
        with open("data{}.json".format(municipio), "w") as json_file:
            json.dump(already_charged, json_file, indent = 4, sort_keys = True)
    except Exception as e:
        print(e)
        with open("data{}.json".format(municipio), "w") as json_file:
            json.dump(data, json_file, indent = 4, sort_keys = True)

