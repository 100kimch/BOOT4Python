import json
import random
from pprint import pprint

with open('4_1_keywords.json') as data_file:
	data = json.load(data_file)

for i in range(5):
	print( str(i) +"조는:")
	for j in range(20):
		print(data[random.randrange(1, 5960)])


