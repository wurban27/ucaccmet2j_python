#1.1 Seatlle station code: GHCND:US1WAKG0038
#1.2
import json
with open('precipitation.json') as file:
    station_data_json = json.load(file)

Seattle_list = []

for dictionary in station_data_json:
    if  dictionary["station"] == "GHCND:US1WAKG0038":
        Seattle_list.append(dictionary)
print(Seattle_list)

#1.3

measurements = [0,0,0,0,0,0,0,0,0,0,0,0]
for measurement in Seattle_list: 
    date = str(measurement['date'])
    split_date=date.split("-") #gives a list of dates splitted by commas (y,m,d)
    month = split_date [1]
    month = int(month)
    index = month -1
    value = measurement["value"]
    measurements[index] += value
print(measurements)

#1.4
Seattle = {}
Seattle["station"] = "GHCND:US1WAKG0038"
Seattle["state"] = "WA"
Seattle["total_monthly_precipation"] = measurements
print(Seattle)

Locations_dict = {}
Locations_dict["Seattle"] = Seattle

with open('results.json', 'w', encoding = 'utf-8') as file:
    json.dump(Locations_dict,file, indent=4)

#1.5 Committed

#2.1
total_yearly_percipation = 0
for entry in Seattle["total_monthly_precipation"]:
    total_yearly_percipation += entry
print(total_yearly_percipation)

#2.2
relative_monthly_percipation = [0,0,0,0,0,0,0,0,0,0,0,0]
index = 0
for element in Seattle["total_monthly_precipation"]:
    relative_monthly_percipation[index] = element/total_yearly_percipation
    index +=1

print(relative_monthly_percipation)

Seattle["total_yearly_percipation"] = total_yearly_percipation
Seattle["relative_monthly_percipation"] = relative_monthly_percipation

print(Locations_dict)

with open('results.json', 'w', encoding = 'utf-8') as file:
    json.dump(Locations_dict,file, indent=4)

#2.3 Commited


3.1
from csv import DictReader
with open('stations.csv') as file:
    stations = DictReader(file)
    stations_list = list(stations)

import json
with open('precipitation.json') as file:
    station_data_json = json.load(file)

index = 0
position= 0
names = []
for name in stations_list:
    names.append(stations_list[index]['Station'])
    
print(names)
def weather_data (names_1):
    
    Location_list = []
    names_1=names[1]
    for dictionary in station_data_json:
        if  dictionary["station"] == names_1:
            Location_list.append(dictionary)
    print(Location_list)






