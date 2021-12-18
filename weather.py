from requests import get
from time import ctime
import json
import sys

if len(sys.argv) < 2:
    print('Usage: python3 weather.py city')
    sys.exit()

api = "7abc90b6e62ee65b20c0b8b02c00e4ee"
url = "http://api.openweathermap.org/data/2.5/weather?"
#city_name = input("Enter city: ")

city_name = ' '.join(sys.argv[1:])
fullUrl = url + "appid=" + api + "&q=" + city_name + "&units=imperial"
response = get(fullUrl)
x = response.json()

sunrise = [ctime(v["sunrise"]) for k,v in x.items() if k == "sys" ]
sunset = [ctime(v["sunset"]) for k,v in x.items() if k == "sys" ]

s,s1 = '',''
for i in sunset: s += i 
s = s.split(' ')[3]

for i in sunrise: s1 += i 
s1 = s1.split(' ')[3]

if x["cod"] != "404":
	name = x["name"]
	y = x["main"]
	current_temperature = y["temp"]
	feels_like = y["feels_like"]
	min = y["temp_min"]
	max = y["temp_max"]
	current_humidity = y["humidity"]
	z = x["weather"]
	weather_description = z[0]["description"]
	print(f"\n\nWeather for {name}")
	print("-------------------------------")
	print(f"description: {weather_description}")
	print(f"current temp: {current_temperature}")
	print(f"feels like: {feels_like}")
	print(f"max: {max}")
	print(f"min: {min}")
	print(f"humidity: {current_humidity}")
	print(f"sunrise: {s1}")
	print(f"sunset: {s}\n\n\n")


else:
	print("City Not Found")
