#credits: Matheus Costa/2024
#access my GitHub here: https://github.com/theus006/Projetos-e-Ideias/blob/main/Python/GetTemp.py

from requests import get
import json

def dataInsert():
    latitude = input("Insert your latitude: ")
    longitude = input("Insert your longitude: ")
    #print("\nlatitude:", latitude)
    #print("longitude:", longitude)
    #get request in API open-meteo.com with your parameters
    getData = get('https://api.open-meteo.com/v1/forecast?latitude='+latitude+'&longitude='+longitude+'&current=temperature_2m&timezone=auto')
    #verifing if one of the parameters is invaild:
    if not "current" in getData.text:
        print("Request error...\n")
        dataInsert()
    else:
        working(getData)
    
def working(getData):
    jsonGet = json.loads(getData.text)
    #http response:
    #print(getData.text)
    #breaking the JSON response:
    currentGet = jsonGet["current"]
    timeGet = currentGet["time"]
    tempGet = currentGet["temperature_2m"]
    fahrenheit = (float(tempGet)*9/5) + 32
    #2 decimal numbers for fahrenheit
    print("\nThe temperature in your region is", tempGet, "°C or",format(fahrenheit, ".2f"),"°F at", timeGet[11:16])
    
    
dataInsert()
