import requests
import json
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
print ("LED for output")
GPIO.setup(2, GPIO.OUT)
GPIO.output(2, False)
GPIO.setup(3, GPIO.OUT)
GPIO.output(3, False)
GPIO.setup(4, GPIO.OUT)
GPIO.output(4, False)
GPIO.setup(17, GPIO.OUT)
GPIO.output(17, False)
GPIO.setup(27, GPIO.OUT)
GPIO.output(27, False)
GPIO.setup(22, GPIO.OUT)
GPIO.output(22, False)
GPIO.setup(5, GPIO.OUT)
GPIO.output(5, False)
GPIO.setup(6, GPIO.OUT)
GPIO.output(6, False)
GPIO.setup(13, GPIO.OUT)
GPIO.output(13, False)
GPIO.setup(10, GPIO.OUT)
GPIO.output(10, False)
GPIO.setup(9, GPIO.OUT)
GPIO.output(9, False)
GPIO.setup(11, GPIO.OUT)
GPIO.output(11, False)

r= requests.get( "http://api.openweathermap.org/data/2.5/weather?q=Seoul,kr&appid=84c84b95b8315afa208b27b48ca91f55")
r = json.loads(r.content.decode('utf-8').replace("'",'"'))
print(r['weather'][0]['id'])
wid = r['weather'][0]['id']


if wid//100 == 8:
    if wid/100 > 8:
        print("Clouds,red")
        GPIO.output(2, True)
        GPIO.output(17, True)
        GPIO.output(5, True)
        GPIO.output(10, True)
    else:
        print("Clear,margenta")
        GPIO.output(2, True)
        GPIO.output(4, True)
        GPIO.output(17, True)
        GPIO.output(22, True)
        GPIO.output(5, True)
        GPIO.output(13, True)
        GPIO.output(10, True)
        GPIO.output(11, True)


elif wid//100 == 7:
    print("Atmosphere,green")
    GPIO.output(3, True)
    GPIO.output(27, True)
    GPIO.output(6, True)
    GPIO.output(9, True)

elif wid//100 == 6:
    print("Snow,yellow")
    GPIO.output(2, True)
    GPIO.output(17, True)
    GPIO.output(5, True)
    GPIO.output(10, True)
    GPIO.output(3, True)
    GPIO.output(27, True)
    GPIO.output(6, True)
    GPIO.output(9, True)    

elif wid//100 == 5:
    print("Rain,blue")
    GPIO.output(4, True)
    GPIO.output(22, True)
    GPIO.output(13, True)
    GPIO.output(11, True)

elif wid//100 == 3:
    print("Clear,cyan")
    GPIO.output(3, True)
    GPIO.output(27, True)
    GPIO.output(6, True)
    GPIO.output(9, True)
    GPIO.output(4, True)
    GPIO.output(22, True)
    GPIO.output(13, True)
    GPIO.output(11, True)    

elif wid//100 == 2:
    print("Thunderstorm,white")
    GPIO.output(2, True)
    GPIO.output(17, True)
    GPIO.output(5, True)
    GPIO.output(10, True) 
    GPIO.output(3, True)
    GPIO.output(27, True)
    GPIO.output(6, True)
    GPIO.output(9, True)
    GPIO.output(4, True)
    GPIO.output(22, True)
    GPIO.output(13, True)
    GPIO.output(11, True)       

else:
    print("Error getting api data")
    for j in range(1,400):
        for i in range(2,4):
            GPIO.output(i, True)
            timesleep(1/10)
            GPIO.output(i, False)
            timesleep(1/10)

timesleep(10)
GPIO.clean.up()