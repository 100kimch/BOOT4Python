import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
print "LED를 출력으로 설정합니다."

# for rygb led
# lamps = [[2, 3, 4], [17, 27, 22, 10], [9, 11, 5], [6, 13], [19, 26]]

# for rgb led
lamps = [[2, 3, 4], [17, 27, 22], [10, 9, 11], [5, 6, 13], [16, 20, 21]]

def reset_all(lamps):
    GPIO.cleanup()
    for lamp in lamps:
        for (key, value) in enumerate(lamp):
            GPIO.setup(i, GPIO.OUT)
            if key == 0:
                GPIO.output(value, True)
            else:
                GPIO.output(value, False)

def reset_lamps(lamp):
    for i in lamp:
        GPIO.output(i, False)

# mode = int in {'정지': 0, '주의': 1, '좌회전': 2, '직진': 3}
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
        GPIO.output(lamp[1], True)
    elif mode == 3:
        GPIO.output(lamp[2], True)

reset_all(lamps)
time.sleep(1)
set_color(1, lamps[0])
set_color(2, lamps[1])
set_color(3, lamps[2])

time.sleep(3)

reset_all(lamps)

raw_input('press enter to exit program') GPIO.cleanup()
