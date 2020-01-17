# import functions
import random

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