import csv, json, os

csvFilePath1 = r"C:\Users\Lenovo\Documents\MyPYProjects\Week5&6\profile.csv"
jsonFilePath1 = r"C:\Users\Lenovo\Documents\MyPYProjects\Week5&6\output.json"


def csvTojson(csvFilePath1, jsonFilePath1):
    data = {}

    with open(csvFilePath1, encoding='utf-8') as csvFile:


        csvReader = csv.DictReader(csvFile)
        
        data = [row for row in csvReader]


    with open(jsonFilePath1, 'w', encoding='utf-8') as jsonFile:
        jsonFile.write(json.dumps(data, indent=4))


csvFilePath2 = r"C:\Users\Lenovo\Documents\MyPYProjects\Week5&6\output.csv"
jsonFilePath2 = r"C:\Users\Lenovo\Documents\MyPYProjects\Week5&6\input.json"

def jsontocsv(jsonFilePath2, csvFilepath2):
    with open(jsonFilePath2) as jsonFile2:
        data = json.load(jsonFile2)

    playerData = data['players']
    with open(csvFilepath2, 'w') as outputFile:
        writeCsv = csv.writer(outputFile)

        header = playerData[0].keys()
        writeCsv.writerow(header)

        for player in playerData:
            writeCsv.writerow(player.values())



csvTojson(csvFilePath1, jsonFilePath1)
jsontocsv(jsonFilePath2, csvFilePath2)
