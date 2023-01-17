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



#1.5

