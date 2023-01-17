#1.1 Seatlle station code: GHCND:US1WAKG0038
#1.2
import json
with open('precipitation.json') as file:
    station_data_json = json.load(file)

Seattle = []

for dictionary in station_data_json:
    if  dictionary["station"] == "GHCND:US1WAKG0038":
        Seattle.append(dictionary)
print(Seattle)

#1.3

measurements = [0,0,0,0,0,0,0,0,0,0,0,0]
for measurement in Seattle:
    date = str(measurement['date'])
    split_date=date.split("-") #gives a list of dates splitted by commas (y,m,d)
    month = split_date [1]
    month = int(month)
    index = month -1
    value = measurement["value"]
    measurements[index] += value
print(measurements)

#1.4
Seattle_precipation = {}
Seattle_precipation["name"] : "Seattle_station"

for entry in measurements:
    if entry not in  Seattle_precipation:
        Seattle_precipation["Precipation_per_month"] : entry
    
    

print(Seattle_precipation)




