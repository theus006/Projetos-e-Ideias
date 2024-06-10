from requests import get
import json

def dataInsert():
    latitude = input("insert your latitude: ")
    longitude = input("insert your longitude: ")

    print("\nlatitude:", latitude)
    print("longitude:", longitude)
    getData = get('https://api.open-meteo.com/v1/forecast?latitude='+latitude+'&longitude='+longitude+'&current=temperature_2m&timezone=auto')
    if not "current" in getData.text:
        print("Request error...\n")
        dataInsert()
    else:
        working(getData)
    
def working(getData):
    jsonGet = json.loads(getData.text)
    currentGet = jsonGet["current"]
    timeGet = currentGet["time"]
    tempGet = currentGet["temperature_2m"]
    print("\nThe temperature in your region is", tempGet, "°C at", timeGet[11:16])
    
    
dataInsert()

