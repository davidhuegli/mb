import RPi.GPIO as GPIO
import time
from w1thermsensor import W1ThermSensor
sensor = W1ThermSensor()

GPIO.setwarnings(False)

P_RED = 11     # adapt to your wiring
P_GREEN = 13   # ditto
P_BLUE = 15    # ditto
fPWM = 50      # Hz (not higher with software PWM)

cold = 22
hot = 23

def setup():
    global pwmR, pwmG, pwmB
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(P_RED, GPIO.OUT)
    GPIO.setup(P_GREEN, GPIO.OUT)
    GPIO.setup(P_BLUE, GPIO.OUT)
    pwmR = GPIO.PWM(P_RED, fPWM)
    pwmG = GPIO.PWM(P_GREEN, fPWM)
    pwmB = GPIO.PWM(P_BLUE, fPWM)
    pwmR.start(0)
    pwmG.start(0)
    pwmB.start(0)
    
def setColor(r, g, b):
    pwmR.ChangeDutyCycle(int(r / 255 * 100))
    pwmG.ChangeDutyCycle(int(g / 255 * 100))
    pwmB.ChangeDutyCycle(int(b / 255 * 100))

setup()

red = 0
green = 0
blue = 0
setColor(0, 0, 0)

while True:
    temperature = sensor.get_temperature()
    print("The temperature is %s celsius" % temperature)
    if temperature <= cold:
        setColor(0, 0, 255)
    elif temperature > hot:
        setColor(255, 0, 0)
    elif temperature >= hot:
        setColor(255, 0, 0)
    else:
        setColor(255, 255, 0)
    
    
    
    time.sleep(1)