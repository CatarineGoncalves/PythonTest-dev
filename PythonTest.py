import csv
import json
import os.path

csv_file_name = "c:/PythonTest/jodi_gas_beta.csv"
json_file_name = os.path.join("c:/PythonTest", "resultado.json")

print(f'Processando o arquivo {csv_file_name}')

try:
    arquivo_json = open(json_file_name, 'w')

    with open(csv_file_name) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        next(readCSV)
        for row in readCSV:
            data = {} #Dictionary que irá armazenar o conteúdo de cada linha
            points = [] #Lista para armazenar data e numero
            fields = {} #Dictionary com os Metadados
            data["series_id"] = "jodi_gas_beta"
            points.append([row[1], row[5]])
            fields["REF_AREA"] = row[0]
            fields["ENERGY_PRODUCT"] = row[2]
            fields["FLOW_BREAKDOWN"] = row[3]
            fields["UNIT_MEASURE"] = row[4]
            fields["ASSESSMENT_CODE"] = row[6]
            data["points"] = points
            data["fields"] = fields
            json.dump(data, arquivo_json) #Converter a linha para json
            arquivo_json.write('\n') #Salvar o arquivo.

    arquivo_json.close()

    print(f'Fim do processamento do arquivo {csv_file_name}, gerado o arquivo {json_file_name}')    
    
except Exception as e:
    raise e
