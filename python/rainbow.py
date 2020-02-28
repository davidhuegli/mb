# Imports
import os
import random
import time
import RPi.GPIO as GPIO

GPIO.setwarnings(False)

P_RED = 11     # adapt to your wiring
P_GREEN = 13   # ditto
P_BLUE = 15    # ditto
fPWM = 50      # Hz (not higher with software PWM)

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

status = 2
while True:
    

    if status == 1:
        if blue > 0:
            blue = blue - 1
        else:
            status = 2

    if status == 2:
        if blue < 255:
            blue = blue + 1
        else:
            status = 3

    if status == 3:
        if red > 0:
            red = red - 1
        else:
            status = 4

    if status == 4:
        if green < 255:
            green = green + 1
        else:
            status = 5
    
    if status == 5:
        if blue > 0:
            blue = blue - 1
        else:
            status = 6

    if status == 6:
        if red < 255:
            red = red + 1
        else:
            status = 7

    if status == 7:
        if green > 0:
            green = green - 1
        else:
            status = 1

    setColor(red, green, blue)
    time.sleep(1)