import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
print "Setup LED pins as outputs"

# for rygb led
# lamps = [[2, 3, 4], [17, 27, 22, 10], [9, 11, 5], [6, 13], [19, 26]]

# for rgb led
lamps = [[2, 3, 4], [17, 27, 22], [10, 9, 11], [5, 6, 13], [16, 20, 21]]

def reset_all(lamps):
    GPIO.cleanup()
    for lamp in lamps:
        for (key, value) in enumerate(lamp):
            GPIO.setup(value, GPIO.OUT)
            if key == 0:
                GPIO.output(value, True)
            else:
                GPIO.output(value, False)

def reset_lamps(lamp):
    for i in lamp:
        GPIO.output(i, False)

# mode = int in {'stopped': 0, 'warning': 1, 'left': 2, 'straight': 3}
# def set_color(mode, lamp):
#     reset_lamps(lamp)
#     if mode == 0:
#         GPIO.output(lamp[0], True)
#     else:
#         length = len(lamp)
#         if length == 2 and mode == 4:
#             GPIO.output(lamp[1], True)
#         elif length == 3:
#             if mode == 1:
#                 GPIO.output(lamp[1], True)
#             elif mode == 2 or mode == 3:
#                 GPIO.output(lamp[2], True)
#         else:
#             GPIO.output(lamp[mode], True)
def set_color(mode, lamp):
    reset_lamps(lamp)
    if mode == 0:
        GPIO.output(lamp[0], True)
    elif mode == 1:
        GPIO.output(lamp[0], True)
        GPIO.output(lamp[1], True)
    elif mode == 2:
        GPIO.output(lamp[2], True)
    elif mode == 3:
        GPIO.output(lamp[1], True)

def blink(blinkSeconds, lamp):
    status = True
    while blinkSeconds <= 0:
        status != status
        GPIO.output(lamp[1], status)
        time.sleep(0.5)
        blinkSeconds -= 0.5
 
reset_all(lamps)
time.sleep(1)

set_color(3, lamps[0])
set_color(3, lamps[1])
blink(10, lamps[4])

set_color(1, lamps[0])
set_color(1, lamps[1])
set_color(0, lamps[4])
time.sleep(3)

set_color(0, lamps[0])
set_color(2, lamps[1])
time.sleep(5)

set_color(1, lamps[1])
time.sleep(3)

set_color(0, lamps[1])
set_color(2, lamps[2])
set_color(3, lamps[3])
time.sleep(5)

set_color(1, lamps[2])
set_color(0, lamps[3])
time.sleep(3)

reset_all(lamps)

raw_input('press enter to exit program')
GPIO.cleanup()
