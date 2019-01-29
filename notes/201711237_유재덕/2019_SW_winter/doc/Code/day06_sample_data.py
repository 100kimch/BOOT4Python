import json

with open('./day06_sample_API.json') as data_file:
    data = json.load(data_file)
    toCelsius = data['main']['temp']
    weather = data['weather'][0]['main']
    print(toCelsius)
    print(weather)

