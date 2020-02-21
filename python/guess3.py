# import modules
import random
import RPi.GPIO as GPIO
import time

# GPIO Settings
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)

# own functions
def blinkLed(count) :
    for i in range(0,count):
        GPIO.output(17, 1)
        time.sleep (0.5)
        GPIO.output(17, 0)
        time.sleep (0.5)

# define range of the number
randomNumber = random.randrange(0,100)

# print start text
print("Random number has been generated")

# define Variable
guessed = False

# start the Game
while guessed==False:

    # read guess from player and check the input
    userInput = int(input("Your guess please: "))
    if userInput==randomNumber:
        guessed = True
        print("Well done!")
        blinkLed(10)
    elif userInput>100:
        print("Our guess range is between 0 and 100, please try a bit lower")
    elif userInput<0:
        print("Our guess range is between 0 and 100, please try a bit higher")
    elif userInput>randomNumber:
        print("Try one more time, a bit lower")
    elif userInput < randomNumber:
        print("Try one more time, a bit higher")

# finish the program
print("End of program")