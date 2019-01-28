import json

with open('./api_weather.json') as data_file:
    data = json.load(data_file)
    toCelsius = data['main']['temp']-273
    weather = data['weather'][0]['main']
    print(toCelsius)
    print(weather)