import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

TRIG = 19
ECHO = 13

print("Distance measurement in progress")

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

try:
    while True:
        GPIO.output(TRIG, False)
        time.sleep(2)

        # Send trigger pulse
        GPIO.output(TRIG, True)
        time.sleep(0.00001)
        GPIO.output(TRIG, False)

        # Measure echo time
        while GPIO.input(ECHO) == 0:
            pulse_start = time.time()

        while GPIO.input(ECHO) == 1:
            pulse_end = time.time()

        pulse_duration = pulse_end - pulse_start

        # Calculate distance
        distance = pulse_duration * 17150
        distance = round(distance, 2)

        if 2 < distance < 400:
            print("Distance:", distance, "cm")
        else:
            print("Out of range")

except KeyboardInterrupt:
    GPIO.cleanup()