
import json 

with open('sample_api.json') as data_file:
    data = json.load(data_file)
    temp = data['main']['temp'] - 273
    print(temp)
