from time import sleep
import random

#Introduce user to the program
if __name__ == "__main__": #This does a good thing
    print ("*" * 32)
    print("Welcome to the Dice Roller!".center(32))
    print ("*" * 32)
    print()
    sleep(1)

    def roll_dice(diceamnt, diceint): #Defines function roll_dice
        dicetotal = 0 #Reset dicetotal
        for i in range(diceamnt): #Repeat for desired amount of dice rolled
            diceroll = random.randint(1, diceint) #Roll based on type of dice selected
            print(diceroll) #Print each roll as they are rolled
            sleep(1)
            dicetotal = dicetotal + diceroll #Add each dice roll to the total
        return dicetotal


    rolling=True
    while rolling: #Repeats the loop upon each roll unless exited by user
        choosing = True
        while choosing:
            #Prompt user to chose their dice type
            print("*" * 32)
            print("Which type of dice would you like to roll?")
            sleep(1)
            print("You may select from D2, D3, D4, D6, D8, D10, D12, D20, and D100!")
            sleep(1)
            print("You may also type 'exit' to leave the program.")

            dicetype = str(input())  # User enters the type of dice they wish to roll
            if dicetype == "exit": #User wishes to exit the program
                sleep(1)
                print("Thank you for rolling your luck!")
                sleep(2)
                rolling = False  # exits the while loop
            elif dicetype == "D2" or dicetype == "D3" or dicetype == "D4" or dicetype == "D6" or dicetype == "D8" or dicetype == "D10" or dicetype == "D12" or dicetype == "D20" or dicetype == "D100":
                diceint = int(dicetype[1:]) #Extracts the dicetype as an integer
                choosing = False
            else:
                print("Uh oh! It looks like you entered an invalid dice type!")
                sleep(1)
                #exit() #Exits the program because exiting the loop wasn't working lmao
            sleep(1)

        print("How many", dicetype, "would you like to roll?")
        diceamnt = int(input())  # User enters number of dice to roll
        sleep(1)

        dicetotal = roll_dice(diceamnt, diceint) #Set the returned value to dicetotal
        print("You rolled a total of", dicetotal, "!") #Print the total in a clear statement
        sleep(2)


