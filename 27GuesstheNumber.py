#Number Guesser
#Olivia Kulinski
import random

def guessNumber(): #Function in which you get one try to guess a number 1 - 10 and shows what the number was.
    print("Welcome to number guesser! In this game you need to guess what the number is from 0-10")
    guessingNumber = int(input("Enter Number"))
    secretNumber = random.randint(0,10)
    if guessingNumber == secretNumber:
        print("YOU WIN THANKS FOR PLAYING NUMBER GUESSER")
    else:
        print("You lost" + " " + "The Number was" + " " + str(y))

def guessNumber_Difficulty(): #Function in which you guess a number 1-10 with three guesses and tells you whether your guess is too low or too high.
    print("Welcome to number guesser! In this game you need to guess what the number is from 0-10 in 3 guesses")
    z = input("Choose Your Difficulty: Easy Medium Hard")
    guessingNumber = int(input("Enter Number"))
    secretNumber = random.randint(0,10)
    if guessingNumber == secretNumber:
        print("YES, YOU WIN! THANKS FOR PLAYING NUMBER GUESSER")
        print("Would you like to play again?")
        a = input("Would you like to play again?")
    elif guessingNumber < secretNumber:
        print("Too Low, Try again!")
        guessingNumber = int(input("Second Guess:"))
        if guessingNumber == secretNumber:
            print("You got it!! Thanks for playing!")
            print("Would you like to play again?")
            a = input("Would you like to play again?")
        elif guessingNumber < secretNumber:
            print("Too Low, Try again!")
            guessingNumber = int(input("Third Guess:"))
            if guessingNumber == secretNumber:
                print("You got it!! Thanks for playing!")
                print("Would you like to play again?")
                a = input("Would you like to play again")
            elif guessingNumber != secretNumber:
                print("Sorry, you didn't get it. Would you like to play again?")
                print("Would you like to play again?")
                a = input("Would you like to play again")
        elif guessingNumber > secretNumber:
            print("Too High, Try again!")
            guessingNumber = int(input("Third Guess:"))
            if guessingNumber == secretNumber:
                print("You got it!! Thanks for playing!")
                print("Would you like to play again?")
                a = input("Would you like to play again?")
            elif guessingNumber != secretNumber:
                print("Sorry, you didn't get it. Would you like to play again?")
                a = input("Would you like to play again?")
        elif guessingNumber !=secretNumber:
            print("Sorry, you didn't get it. Would you like to play again?")
            a = input("Would you like to play again?")
    elif guessingNumber > secretNumber:
        print("Too High, Try again!")
        guessingNumber = int(input("Second Guess:"))
        if guessingNumber == secretNumber:
            print("You got it!! Thanks for playing!")
            print("Would you like to play again?")
            a = input("Would you like to play again?")
        elif guessingNumber < secretNumber:
            print("Too Low, Try again!")
            guessingNumber = int(input("Third Guess:"))
            if guessingNumber == secretNumber:
                print("You got it!! Thanks for playing!")
                print("Would you like to play again?")
                a = input("Would you like to play again?")
            elif guessingNumber != secretNumber:
                print("Sorry, you didn't get it. Would you like to play again?")
                a = str(input("Would you like to play again?"))
        elif guessingNumber > secretNumber:
            print("Too High, Try again!")
            guessingNumber = int(input("Third Guess:"))
            if guessingNumber == secretNumber:
                print("You got it!! Thanks for playing!")
                print("Would you like to play again?")
                a = input("Would you like to play again?")
            elif guessingNumber != secretNumber:
                print("Sorry, you didn't get it. Would you like to play again?")
                a = input("Would you like to play again?")

    if a == "yes": #runs the game again
        guessNumber_Difficulty()
    else:
        print("Okay, thank you for playing!")



#Main
#guessNumber()
guessNumber_Difficulty()
