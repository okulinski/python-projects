#Rock Paper Scissors
#Olivia Kulinski
#1.6.25

#Initialization
import random

#functions
def rockpaperscissors():
    wins = 0
    losses = 0
    ties = 0
    while True:

        aioption = random.randint(1,3)
        if aioption == 1:
            aioption = "rock"
        elif aioption ==2:
            aioption = "paper"
        elif aioption == 3:
            aioption = "scissors"
        choice = input("Select an option: rock, paper, scissors, or quit")
        if choice != "rock" or choice != "scissors" or choice != "paper":
            print("Please enter a valid option")
        if aioption == "rock" and choice == "rock":
            print("Computer: " + aioption)
            print("You: " + choice)
            print("Tie")
            ties = ties + 1
        elif aioption == "rock" and choice == "scissors":
            print("Computer: " + aioption)
            print("You: " + choice)
            print("You lost")
            losses = losses + 1
        elif aioption == "rock" and choice == "paper":
            print("Computer: " + aioption)
            print("You: " + choice)
            print("You won!")
            wins = wins + 1
        elif aioption == "scissors" and choice == "rock":
            print("Computer: " + aioption)
            print("You: " + choice)
            print("You Won!")
            wins = wins + 1
        elif aioption == "scissors" and choice == "scissors":
            print("Computer: " + aioption)
            print("You: " + choice)
            print("Tie")
            ties = ties + 1
        elif aioption == "scissors" and choice == "paper":
            print("Computer: " + aioption)
            print("You: " + choice)
            print("You Lost")
            losses = losses + 1
        elif aioption == "paper" and choice == "rock":
            print("Computer: " + aioption)
            print("You: " + choice)
            print("You Lost!")
            losses = losses + 1
        elif aioption == "paper" and choice == "scissors":
            print("Computer: " + aioption)
            print("You: " + choice)
            print("You Won!")
            wins = wins + 1
        elif aioption == "paper" and choice == "paper":
            print("Computer: " + aioption)
            print("You: " + choice)
            print("Tie")
            ties = ties + 1
        elif choice == "quit":
            print("You had " + str(wins) + " wins")
            print("You had " + str(losses) + " losses")
            print("You had " + str(ties) + " ties")
            ans = input("Would you like to play again?")
            if ans == "yes":
                rockpaperscissors()
            if ans == "no":
                print("Okay, Thank You for playing!!")
            break
#main
print("Welcome to Rock Paper Scissors")
print("You will be playing a game or Rock Paper Scissors against the computer")
print("Select an option")
rockpaperscissors()
