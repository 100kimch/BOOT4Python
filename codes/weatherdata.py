import requests
import json
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
print ("LED for output")
GPIO.setup(23, GPIO.OUT)
GPIO.output(23, False)
GPIO.setup(24, GPIO.OUT)
GPIO.output(24, False)
GPIO.setup(25, GPIO.OUT)
GPIO.output(25, False)

r= requests.get( "http://api.openweathermap.org/data/2.5/weather?q=Seoul,kr&appid=84c84b95b8315afa208b27b48ca91f55")
r = json.loads(r.content.decode('utf-8').replace("'",'"'))
print(r['weather'][0]['id'])
wid = r['weather'][0]['id']


if wid//100 == 8:
    if wid/100 > 8:
        GPIO.output(23, True)
    else:
        GPIO.output(24, True)


elif wid//100 == 7:
    GPIO.output(25, True)
          
else:
    GPIO.output(23, True)
    GPIO.output(24, True)



