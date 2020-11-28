# Please note that this is an improvised version of the solution of Project C-97 of PRO level WhiteHatJunior.
# This includes guesses between 1 and 100. Also you can claim hints and get points
# Enjoy!
import random
point = 101
randomint = random.randint(1,100)
hintflag = 0
hintmessage = "To claim a hint, enter 102 in the input below. ***THE HINT WILL COME AT A COST OF 20 POINTS***"
guessflag = 0
def init():
    global guess, point, guessflag
    point = point - 1
    guessflag = guessflag + 1
    print('')
    print(hintmessage)
    guess = int(input("Enter your guess. It should be between 1 and 100... "))
    proceed()

def proceed():
    global hintflag
    global guessflag
    global point
    if (guess < 1 or (guess > 100 and guess != 102)):
        print('')
        print("Please enter a number between 1 and 100... ")
        guessflag = guessflag-1
        point = point + 1
        init()
    elif ((guess == 102)and(hintflag < 2 and hintflag >= 0)):
        if(hintflag == 0):
            checkrandeven()
        if(hintflag == 1):
            checkrandmultiple3()
    else:
        match()

def checkrandmultiple3():
    if (randomint % 3 == 0):
        global israndmultiple3, point, hintmessage, hintflag, guessflag
        hintflag = hintflag + 1
        israndmultiple3 = True
        point = point-19
        guessflag = guessflag - 1
        hintmessage = 'You have exhausted all your hints'
        print('')
        print("Your hint is...")
        print("The number to be guessed is a multiple of 3.")
        print("***YOU HAVE SPENT 20 POINTS***")
        init()
    else:
        hintflag = hintflag+1
        israndmultiple3 = False
        point = point-19
        guessflag = guessflag - 1
        hintmessage = 'You have exhausted all your hints'
        print('')
        print("Your hint is...")
        print("The number to be guessed is not a multiple of 3.")
        print("***YOU HAVE SPENT 20 POINTS***")
        init()

def checkrandeven():
    if (randomint % 2 == 0):
        global israndeven, point, hintmessage, hintflag,guessflag
        hintflag = hintflag+1
        israndeven = True
        point = point-19
        guessflag = guessflag - 1
        hintmessage = 'To claim your ***LAST*** hint, enter 102 in the input below. ***THE HINT WILL COME AT A COST OF 20 POINTS***'
        print('')
        print("Your hint is...")
        print("The number to be guessed is even.")
        print("***YOU HAVE SPENT 20 POINTS***")
        init()
    else:
        israndeven = False
        hintflag = hintflag+1
        point = point-19
        guessflag = guessflag - 1
        hintmessage = 'To claim your ***LAST*** hint, enter 102 in the input below. ***THE HINT WILL COME AT A COST OF 20 POINTS***'
        print('')
        print("Your hint is...")
        print("The number to be guessed is odd.")
        print("***YOU HAVE SPENT 20 POINTS***")
        init()

def match():
    global randomint, guess, point, guessflag, hintflag
    if(randomint != guess):
        if(randomint < guess):
            print("")
            print("Try Again! Your number was too high; Try a number lower than "+str(guess))
        if(randomint > guess):
            print("")
            print("Try Again! Your number was too low; Try a number higher than "+str(guess))
    if(randomint == guess):
        print("")
        print ("CONGRATULATIONS! You won!")
        print ("It took you "+ str(guessflag) + " tries, "+ str(hintflag)+" hints to beat the game!")
        print("The number of points you finished with are...")
        print(point)
        print("Thanks for playing!")
        exit()

while guessflag <=10:
    print("You currently have 100 points. Try to finish the game with as many points as possible!")
    print("YOU GET AT MOST 10 CHANCES TO BEAT THE GAME")
    print(randomint)
    init()
else:
    print('')
    print('GAME OVER!')
    print("You Lose!")
    print("The random number was "+ str(randomint)+ " and your last guess was "+ str(guess)+".")