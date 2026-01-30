import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)

leds = [11,12,35,38]
inputs = [15,16,18,22]

for led in leds:
    GPIO.setup(led, GPIO.OUT)
    GPIO.output(led, GPIO.LOW)  

for button in inputs:
    GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


try:
    while True:
        for i in range(len(inputs)):
            if GPIO.input(inputs[i]) == GPIO.HIGH:
                GPIO.output(leds[i], GPIO.HIGH)
            else:
                GPIO.output(leds[i], GPIO.LOW)
        time.sleep(0.05)
except KeyboardInterrupt:
    pass

finally:
    GPIO.cleanup()
